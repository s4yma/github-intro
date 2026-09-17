import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

os.makedirs("images", exist_ok=True)

url = "https://shohozbiggan.github.io/home/"

response = requests.get(url)
print(response.text)
soup = BeautifulSoup(response.text, "html.parser")

img = soup.select("img")

for i in img:
    src = i.get("src")
    print(src)

    if not src:
        continue

    img_url = urljoin(url, src)
    data = requests.get(img_url).content

    filename = img_url.split("/")[-1]

    with open(f"images/{filename}", "wb") as f:
        f.write(data)