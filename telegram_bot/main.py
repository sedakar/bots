import telegram
import asyncio
import os


async def send_message(message, TOKEN, CHAT_ID):
    bot = telegram.Bot(TOKEN)
    if  CHAT_ID != None:
        await bot.sendMessage(CHAT_ID, message, parse_mode=telegram.constants.ParseMode.MARKDOWN,
                                disable_notification=True)
    else:
        await bot.sendMessage(CHAT_ID, message, parse_mode=telegram.constants.ParseMode.MARKDOWN,
                                disable_notification=True)

if __name__ == "__main__":

    CHAT_ID = os.getenv("CHAT_ID")
    TOKEN = os.getenv("TOKEN")

    message = "Hello, I am Seda."
    asyncio.run(send_message(message, TOKEN, CHAT_ID))