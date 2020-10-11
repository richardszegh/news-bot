from news_bot.bot.hwsw import HwswBot
from news_bot.bot.hvg import HvgBot


def main():
    hvgBot = HvgBot(["IbM", "Samsung"])
    hvgBot.parse()


if __name__ == "__main__":
    main()
