from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

number = driver.find_element(By.CSS_SELECTOR, "span#mwDw")
#number.click()

all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
#all_portals.click()

search_button = driver.find_element(By.CSS_SELECTOR, "#p-search a")
search_button.click()

search = driver.find_element(By.ID, "searchInput")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.quit()