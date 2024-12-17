from aiogram.types import Message
from database.db import DataBase
from dispatcher import dp

db = DataBase()

@dp.message_handler(commands=['get_admins'], state="*")
async def get_admins(msg: Message):
    channels = db.get_channels()

    if not channels:
        await msg.answer("Список администраторов пуст.")
        return
    
    for channel in channels:
        channel_list = "\n".join(
            f"ID: {channel[0]}: <a href='{channel[2]}'>{channel[1]}</a>"
        )
    
    await msg.answer(f"Список каналов:\n{channel_list}")
