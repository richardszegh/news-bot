import requests
from bs4 import BeautifulSoup


class IndexBot:
    def __init__(self, keywords):
        self.markup = requests.get("https://index.hu/24ora/").text
        self.keywords = keywords
        self.results = []

    def parse(self):
        soup = BeautifulSoup(self.markup, "html.parser")
        news = soup.findAll("article", {"class": "rovatajanlo"})
        for news_item in news:
            title = (
                news_item.find("a", {"class": "cim"}).text.lower().strip()
                if news_item.find("a", {"class": "cim"})
                else ""
            )
            excerpt = (
                news_item.find("div", {"class": "ajanlo"}).text.lower().strip()
                if news_item.find("div", {"class": "ajanlo"})
                else ""
            )
            for keyword in self.keywords:
                if (keyword.lower() in title) or (keyword.lower() in excerpt):
                    if news_item.find("a", {"class": "cim"}):
                        self.results.append(
                            {
                                "title": title,
                                "link": news_item.find("a", {"class": "cim"})["href"],
                            }
                        )

    def refresh(self):
        self.markup = requests.get("https://index.hu/24ora/").text
        self.parse()
