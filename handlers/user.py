from aiogram import types, Dispatcher
from core import dp, bot, dialogues

async def command_start(message: types.Message):
    await message.answer(dialogues["start"].format(FIRST_NAME=message.from_user.first_name))

async def command_check_my_id(message: types.Message):
    await message.answer(dialogues["myid"].format(USER_ID=message.from_user.id))

def create_user_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_check_my_id, commands=['checkmyid'])