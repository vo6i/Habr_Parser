import requests

from bs4 import BeautifulSoup

URL = "https://habr.com/ru/search/?target_type=posts&q=python&order_by=date"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

post = soup.find("article", class_="tm-articles-list__item", id=True)
post_id = post["id"]
print(post_id)

h2ck = post.find("h2", class_="tm-title tm-title_h2")
title = h2ck.find("span").text.strip() # class_="tm-tittle tm-tittle_h2")
#h2bd = post.find("p")
#psttxt = h2bd.find("p").text.strip()
#description = post.find("div", class_="article-formatted-body article-formatted-body article-formatted-body_version-2").text.strip()
url = post.find("a", class_="tm-title__link", href=True)["href"].strip()

print(title,url)
