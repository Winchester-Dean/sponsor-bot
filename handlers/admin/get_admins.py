from aiogram.types import Message
from database.db import DataBase
from dispatcher import dp

db = DataBase()

@dp.message_handler(commands=['get_admins'], state="*")
async def get_admins(msg: Message):
    admins = db.get_admins()

    if not admins:
        return await msg.answer("Список администраторов пуст.")
    
    for admin in admins:
        admin_list = "\n".join(
            f"ID: {admin[0]}: <a href='https://t.me/user?id={admin[0]}'>{admin[1]}</a>"
        )
    
    await msg.answer(f"Список администраторов:\n{admin_list}")

