import requests
from bs4 import BeautifulSoup

website = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(website)
soup = BeautifulSoup(response.text, "html.parser")

movie_titles = soup.find_all("h3", class_="title")
movie_titles = movie_titles[::-1]  # reverses

with open("movies.txt", "w", encoding="utf-8") as file:
    for title in movie_titles:
        title_text = title.getText().strip()
        file.write(title_text + "\n")