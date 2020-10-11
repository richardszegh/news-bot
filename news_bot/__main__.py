from pprint import pprint
from PyInquirer import prompt
import time

from news_bot.bot.hwsw import HwswBot
from news_bot.bot.hvg import HvgBot
from news_bot.bot.index import IndexBot
from news_bot.util.color import Color


def main():
    answers = {"sites": [], "keywords": [], "interval": 3600}

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

    answers["interval"] = prompt(
        [
            {
                "type": "input",
                "message": "Ilyen gyakorisaggal nezz utana uj hireknek (masodpercben): ",
                "name": "interval",
            }
        ]
    )["interval"]

    activeBots = []
    for site in answers["sites"]:
        if site == "Index":
            activeBots.append(IndexBot(answers["keywords"]))
        elif site == "HVG":
            activeBots.append(HvgBot(answers["keywords"]))
        elif site == "HWSW":
            activeBots.append(HwswBot(answers["keywords"]))

    seen = []
    while True:
        results = []
        for bot in activeBots:
            bot.refresh()
            results.extend(bot.results)
        for result in results:
            if result not in seen:
                currentTime = time.strftime("%Y-%m-%d %H:%M", time.localtime())
                resultInfo = f"{Color.BOLD}{Color.GREEN}[{currentTime}] {Color.END}{Color.BOLD}{Color.CYAN}{result['title'].capitalize()}:{Color.END} {Color.UNDERLINE}{result['link']}{Color.END}"

                print(f"\n{resultInfo}")
                seen.append(result)
        time.sleep(int(answers["interval"]))


if __name__ == "__main__":
    main()
