import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests

load_dotenv()
GOOGLE_FORMS_LINK = os.getenv("GOOGLE_FORMS_LINK")
ZILLOW_LINK = "https://appbrewery.github.io/Zillow-Clone/"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}
response = requests.get(ZILLOW_LINK, headers=header)
soup = BeautifulSoup(response.content, 'html.parser')
property_cards = soup.find_all("article", attrs={"data-test": "property-card"})

listings = []
for card in property_cards:
    addr_tag = card.find("address", attrs={"data-test": "property-card-addr"})
    price_tag = card.find("span", attrs={"data-test": "property-card-price"})
    link_tag = card.find("a", attrs={"data-test": "property-card-link"})

    listings.append({
        "address": addr_tag.get_text(strip=True) if addr_tag else None,
        "price": price_tag.get_text(strip=True) if price_tag else None,
        "url": link_tag["href"] if link_tag else None,
    })

print(listings)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(GOOGLE_FORMS_LINK)
time.sleep(5)

for listing in listings:
    name_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name_input.send_keys(listing["address"])
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(listing["price"])
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(listing["url"])
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
    time.sleep(3)
    next_answer = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    next_answer.click()
    time.sleep(3)

time.sleep(15)
driver.quit()