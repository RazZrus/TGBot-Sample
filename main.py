from aiogram.utils import executor
from core import dp, dialogues, ADMINS, TOKEN, Color

painter = Color()

from handlers import user

user.create_user_handlers(dp)

async def on_startup(_):
    print(painter.color(' [BOT] ', 'black', 'yellow', ['bold']), 'Loaded dialogues:\n', dialogues)
    print(painter.color(' [BOT] ', 'black', 'yellow', ['bold']), 'Loaded admins:\n', ADMINS)
    print(painter.color(' [BOT] ', 'black', 'yellow', ['bold']), 'Working with TOKEN:', TOKEN)
    print(painter.color(' (c) Dmitry Smotryaev 2022 ', 'black', 'red', ['bold']))
    print(painter.color(' [BOT] ', 'black', 'yellow', ['bold']), '- Bot is online!')

async def on_shutdown(_):
    print(painter.color(' [BOT] ', 'black', 'yellow', ['bold']), '- Bot is offline!')
    print(painter.color(' (c) Dmitry Smotryaev 2022 ', 'black', 'red', ['bold']))

executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)