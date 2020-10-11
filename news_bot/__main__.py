from news_bot.bot.hwsw import HwswBot
from news_bot.bot.hvg import HvgBot
from news_bot.bot.index import IndexBot


def main():
    indexBot = IndexBot(["kisteherautó", "térkép"])
    indexBot.parse()


if __name__ == "__main__":
    main()
