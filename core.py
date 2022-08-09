from settings import TOKEN, ADMINS
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from EasyColors import Color

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

with open("texts.txt", "r", encoding="UTF-8") as file:
    file = file.read().split(";")
    dialogues = {}
    for i in file:
        dialogues[i.split("::")[0].strip()] = i.split("::")[1].strip()