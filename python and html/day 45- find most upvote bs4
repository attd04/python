from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
article = (soup.find_all(name='a', rel='noreferrer'))
article_texts = []
article_links = []
for article_tag in article:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_links)
# print(article_texts)
# print(article_upvote)

highest_num = max(article_upvote)
highest_index = article_upvote.index(highest_num)

print(article_texts[highest_index])
