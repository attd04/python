from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
movie_webpage = response.text

soup = BeautifulSoup(movie_webpage, 'html.parser')

movie_titles = [title.getText() for title in soup.find_all(name='h3', class_="title")]
print(movie_titles)

file1 = open('movies1.txt', 'w')
for movies in movie_titles:
    file1.write(movies+"\n")

main_file = open("movies.txt", 'w')
data = file1.readlines()
for movie in reversed(data):
    main_file.write(f"{movie}")
