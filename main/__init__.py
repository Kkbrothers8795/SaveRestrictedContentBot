#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "2532603"
API_HASH = "f565b00bbe3ad9c6748e39a3a71d16e7"
BOT_TOKEN = "7251010457:AAGOemQb-m_U47bRhxgHbWZUhFt7uyCoiOk"
SESSION = "BQAmpPsAwxuT--1jX9xqJ0PkjHlxXrRuqcF-ZjJd_tDXsrT6zo3qtx4f7_lZhoiiI5vu3yU2w2HjktgpJJ8Vyadm9UWlUu-UrIadCzD5ghXTZ9YmQeygTQAXzB0AW2stPfomjspM7q8uwBioSeyoHkBvwkltYdE9w9mwwSXpWf4CuuRvljCkzLSbIxZ7VnYfhSNR0BuZa6y05ziSL-taRULoLQdHN61Hg11j9duOW1r6eT1kC9unpbK1ifCYs6jlPKL1qFP-TXckEa_1_hChiJb0IRvBZCP6IUo29pgE8SqTVe9OGe7m3YNlEBEwECucjgph8QykD903nBqiMNeUM3ihiwNb9wAAAAGhaDiOAA"
FORCESUB = "hxsourcecode"
AUTH = "7002929294"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
