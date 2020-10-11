import requests
from bs4 import BeautifulSoup


class HvgBot:
    def __init__(self, keywords):
        self.markup = requests.get("https://hvg.hu/frisshirek").text
        self.keywords = keywords
        self.results = []

    def parse(self):
        soup = BeautifulSoup(self.markup, "html.parser")
        news = soup.findAll("div", {"class": "text-holder"})
        for news_item in news:
            title = news_item.h1.a.text.lower().strip()
            excerpt = news_item.p.text.lower().strip()
            for keyword in self.keywords:
                if (keyword.lower() in title) or (keyword.lower() in excerpt):
                    self.results.append(f"https://hvg.hu{news_item.h1.a['href']}")
