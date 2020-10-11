from pprint import pprint
from PyInquirer import prompt

from news_bot.bot.hwsw import HwswBot
from news_bot.bot.hvg import HvgBot
from news_bot.bot.index import IndexBot


def main():
    answers = {"sites": [], "keywords": []}

    answers["sites"] = prompt(
        [
            {
                "type": "checkbox",
                "message": "Milyen hiroldalakon keressek hireket neked?",
                "name": "news_sites",
                "choices": [{"name": "Index"}, {"name": "HVG"}, {"name": "HWSW"}],
            }
        ]
    )["news_sites"]

    while True:
        keywordAnswer = prompt(
            [
                {
                    "type": "input",
                    "message": "Kulcsszo ami erdekel teged (ha nem szeretnel tobbet megadni, hagyd uresen es nyomj egy [ENTER]-t): ",
                    "name": "keyword",
                }
            ]
        )
        if len(keywordAnswer["keyword"]) == 0:
            break
        else:
            answers["keywords"].append(keywordAnswer["keyword"])

    activeBots = []
    for site in answers["sites"]:
        if site == "Index":
            activeBots.append(IndexBot(answers["keywords"]))
        elif site == "HVG":
            activeBots.append(HvgBot(answers["keywords"]))
        elif site == "HWSW":
            activeBots.append(HwswBot(answers["keywords"]))

    results = []
    for bot in activeBots:
        bot.parse()
        results.extend(bot.results)

    pprint(results)


if __name__ == "__main__":
    main()
