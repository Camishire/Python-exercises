import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
YOUR_SMTP_ADDRESS = os.getenv("YOUR_SMTP_ADDRESS")
YOUR_EMAIL = os.getenv("YOUR_EMAIL")
YOUR_PASSWORD = os.getenv("YOUR_PASSWORD")

print(repr(YOUR_SMTP_ADDRESS))

url = "https://appbrewery.github.io/instant_pot/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
price = soup.find(name="span", class_="a-offscreen")
price = float(price.text[1:])
print(price)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 100

if price < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )