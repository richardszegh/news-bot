from news_bot.bot.hwsw import HwswBot


def main():
    hwswBot = HwswBot(["IbM", "Samsung"])
    hwswBot.parse()


if __name__ == "__main__":
    main()
