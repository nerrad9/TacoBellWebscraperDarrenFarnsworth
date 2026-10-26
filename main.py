import requests as r
import os
from bs4 import BeautifulSoup as bs

url = "https://tacobell.com"
h = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
page = r.get(url+"/food/", headers=h).content
page = bs(page, "html.parser")
atags = page.find_all("a")
links = [tag["href"] for tag in atags if tag["href"][0:6] == "/food/"]

for link in links:
    print(link)
    try:
        os.mkdir(str(link[6:]))
    except Exception as e:
        print(e)
    page = r.get(url+link, headers = h).content
    page = bs(page, "html.parser")
    imgs = page.find_all("img")
    for img in imgs:
        try:
            name = img["alt"]
            src = img["src"]
            if src[0] == "/" or "cheesy-roll-up" in src:
                continue
            with open(f"{link[6:]}/{name}.jpg", "wb") as file:
                page = r.get(src, headers = h).content
                file.write(page)
        except Exception as e:
            print(e)

