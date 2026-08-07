import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

title_spans = soup.find_all(name="span", class_="titleline")
scores = soup.find_all(name="span", class_="score")

for i, title_span in enumerate(title_spans):
    link_tag = title_span.find("a")
    article_text = link_tag.getText()
    article_link = link_tag.get('href')

    article_upvote = scores[i].getText() if i < len(scores) else "N/A"

    print(article_text)
    print(article_link)
    print(article_upvote)
    print("---")