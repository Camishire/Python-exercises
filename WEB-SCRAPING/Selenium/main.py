from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/ASUS-ROG-Strix-Gaming-Laptop/dp/B0DZZWMB2L?_encoding=UTF8&content-id=amzn1.sym.bd749ccd-05a5-46df-9094-58bcc6398482&dib=eyJ2IjoiMSJ9.sa4bsFUOsBKNESVUhrqkbBolvqGCWycPBeqaPNhN5Lk1YKrb68qGxNJR4oZzRxsxJmD7-OG8d2FkqDkU33R5s2WNK6HMbY44zC-CylA0k4rLfuTpMuEmVd3xVCYZC2aO8rcaTD_PodiyhQtfYusQTi6lw3-MPS63WtzBmvwLYwF-6u8QDNNXyYhhK6gN9iVZN-BxSHAgTpZlRTE4K9nTLgWKyCRDZ18fYZoplbVPwH33-pQo9uEtgcZDILOq8ngZaVhDKFvfe_G2TaadKAqMLC_BR9TlAZh_qAs87tix6QQ.vM3f8JlGwYzG-iu-lYimFGiraJjzYrR2c9MvMJ8WT_Q&dib_tag=se&keywords=gaming&pd_rd_r=8f24ac11-fa93-4b04-a6ee-f5e05357dd7c&pd_rd_w=VSlBu&pd_rd_wg=eqzA7&qid=1786354827&sr=8-2")

price_dollar = driver.find_element(By.CLASS_NAME, value = "a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value = "a-price-fraction")
print (f"{price_dollar.text}.{price_cents.text}")

driver.quit()