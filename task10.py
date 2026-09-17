import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://books.toscrape.com/"

driver= webdriver.Chrome()
driver.get(url)

info1 = []
info2 = []
info3 = []
info4 = []

titles = driver.find_elements(By.CSS_SELECTOR, "img.thumbnail")
prices = driver.find_elements(By.CSS_SELECTOR, "p.price_color")
stock = driver.find_elements(By.CSS_SELECTOR, "p.instock")
rating = driver.find_elements(By.CSS_SELECTOR, "p.star-rating")

for i in titles:
    info1.append(i.get_attribute("alt"))

for i in prices:
    info2.append(i.text)

for i in stock:
    info3.append(i.text)

for i in rating:
    rr= i.get_attribute("class").split(" ")[1]
    info4.append(rr)

data= {
    "Title":info1,
    "Price":info2,
    "Rating":info4,
    "Stock":info3
}

import pandas as pd

df = pd.DataFrame(data)
df.to_csv("books.csv", index=False)
time.sleep(5)