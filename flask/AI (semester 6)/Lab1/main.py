# pip install pandas scikit-learn nltk gradio
# installed the packages: ^^^ through terminal

import pandas as pd
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import re
from collections import Counter
from flask import Flask, render_template, request, jsonify

# load dataset
df = pd.read_csv("seth-data.csv")

# removing words that would interfere w/ defining keywords
stop_words = set(ENGLISH_STOP_WORDS)
custom_stop_words = ENGLISH_STOP_WORDS.union({
    'youre', 'dont', 'im', 'ive', 'wont', 'isnt', 'cant', 'wasnt',
    'doesnt', 'didnt', 'couldnt', 'wouldnt', 'shouldnt', 'hasnt',
    'havent', 'hadnt', 'theres', 'heres', 'whats', 'thats', 'lets',
    'just', 'like', 'want', 'way', 'new', 'youll', 'youve', 'got', 'theyre',
    'really', 'did', 'gets', 'come', 'doing', 'going', 'good', 'better', 'know',
    'need', 'make', 'things', 'think'
})

# -------------------------------
# ------PRE PROCESSING ----------
# -------------------------------

# remove null values
df.dropna(inplace=True)

# make everything lowercase
df['processed_content'] = df['content_plain'].apply(lambda x: x.lower())

# remove punctuation & special characters
df['processed_content'] = df['processed_content'].apply(lambda x: re.sub(r"[^\w\s]", "", x))

# tokenization (split into words)
df['processed_content'] = df['processed_content'].apply(lambda x: x.split())

# remove stop words
df['processed_content'] = df['processed_content'].apply(lambda words: [word for word in words if word not in custom_stop_words])

# list of words back to a string
df['processed_content'] = df['processed_content'].apply(lambda words: " ".join(words))

#print(df.head())

# ----------------------------------
# ------KEYWORD EXTRACTION ----------
# -----------------------------------

# initialize TF-IDF vectorizer
# term frequency inverse document frequency
# analyzes the most significant words
vectorizer = TfidfVectorizer(max_features=10)  # extract top 10 keywords per article

# fit and transform processed content
tfidf_matrix = vectorizer.fit_transform(df['processed_content'])

# get keywords for each article
feature_names = vectorizer.get_feature_names_out()
df['keywords'] = [", ".join([feature_names[i] for i in row.argsort()[-5:]]) for row in tfidf_matrix.toarray()]

# show first few article keywords
#print(df[['processed_content', 'keywords']].head())


# ------------------------------------
# ------ ARTICLE EXTRACTION ----------
# -------------------------------------

# Convert articles into numerical vectors to put into clusters
X = vectorizer.fit_transform(df['processed_content'])

# Apply K-Means clustering groups based on similarity
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
# makes 5 clusters
# 42 sets a fixed seed so same results every time
# runs algorithm 10 times and chooses best clustering

# sorts clusters into groups using k means
df['category_num'] = kmeans.fit_predict(X)

# ----- category labelling -------
# get most common words in each category
category_keywords = {} # initialize dictionary to keep words
for i in range(5):
    cluster_articles = df[df['category_num'] == i]['processed_content']
    # ^ select all keywords of the certain cluster and extract processed text
    all_words = " ".join(cluster_articles).split()
    # ^ join all articles into one text string and split into individual words
    common_words = Counter(all_words).most_common(3)
    # ^ count occurrences of each word and take top 3
    category_keywords[i] = [word for word, count in common_words]
    # ^ save the top 3 words for the certain cluster

# labels based on common words
category_labels = {
    0: "Technology & Internet",
    1: "Business & Marketing",
    2: "Personal Development",
    3: "Health & Lifestyle",
    4: "News & Trends"
}

# map category numbers to labels
df['category'] = df['category_num'].map(category_labels)

# Show sample articles with categories
# print(df[['keywords', 'category']].head(10))


# ----------------------------------
# --- FLASK APP (ARTICLE SEARCH) ---
# ----------------------------------

app = Flask(__name__)


# home page
@app.route('/')
def home():
    return render_template('index.html')


# returning keyword groups
@app.route('/keywords')
def get_keywords():
    keyword_groups = {}

    for index, row in df.iterrows():
        keywords = row['keywords'].split(', ')  # get keywords for article
        for keyword in keywords:
            if keyword not in keyword_groups:
                keyword_groups[keyword] = []  # initialize keyword group
            if len(keyword_groups[keyword]) < 3:  # 3 articles per keyword
                keyword_groups[keyword].append({
                    "title": row['title'],
                    "snippet": row['content_plain'][:50] + "...",  # short preview
                    "category": row['category']
                })

    return jsonify(keyword_groups)


# searching articles based on user input
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    limit = request.args.get('limit', default=5, type=int) # shown article limit default = 5

    # str.contains to search for the entire phrase
    results = df[df['processed_content'].str.contains(query, na=False, case=False)]

    limited_results = results[['content_plain', 'category']].head(limit).to_dict(orient='records')
    return render_template('results.html', query=query, results=limited_results, total=len(results))


if __name__ == '__main__':
    app.run(debug=True)



