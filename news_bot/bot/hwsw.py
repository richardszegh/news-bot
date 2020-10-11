import requests
from bs4 import BeautifulSoup


class HwswBot:
    def __init__(self, keywords):
        self.markup = requests.get("https://www.hwsw.hu/hirachivum?page=1").text
        self.keywords = keywords
        self.results = []

    def parse(self):
        soup = BeautifulSoup(self.markup, "html.parser")
        news = soup.findAll("div", {"class": "news-content"})
        for news_item in news:
            title = news_item.a.text.lower().strip() if news_item.find("a") else ""
            excerpt = (
                news_item.span.text.lower().strip() if news_item.find("span") else ""
            )
            for keyword in self.keywords:
                if (keyword.lower() in title) or (keyword.lower() in excerpt):
                    if news_item.find("a"):
                        self.results.append(news_item.a["href"])

    def refresh(self):
        self.markup = requests.get("https://www.hwsw.hu/hirachivum?page=1").text
        self.parse()
