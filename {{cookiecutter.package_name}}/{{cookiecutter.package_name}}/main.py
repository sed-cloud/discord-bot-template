import os

def main():
    """"""
    token: str = os.getenv("DISCORD_RITOMAN_BOT", None)
    if token is None:
        logger.critical("Failed to load Discord bot token.")
        raise Exception("Failed to load Discord bot token.")

    # discord_bot.run(token)

if __name__ == "__main__":
    main()