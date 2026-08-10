from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(2)

language_select_button = driver.find_element(By.CSS_SELECTOR, "#langSelect-EN")
language_select_button.click()
time.sleep(2)

cookie = driver.find_element(By.CSS_SELECTOR, "#bigCookie")

def get_price(product_id):
    price_element = driver.find_element(By.ID, f"productPrice{product_id}")
    price_text = price_element.text.replace(",", "")
    return float(price_text)

def buy_best_upgrade():
    for product_id in range(3):
        try:
            product = driver.find_element(By.ID, f"product{product_id}")
            if "disabled" not in product.get_attribute("class"):
                product.click()
                return
        except:
            continue

time_now = time.time()

while True:
    cookie.click()
    if time.time() - time_now >= 5:
        buy_best_upgrade()
        time_now = time.time()

driver.quit()