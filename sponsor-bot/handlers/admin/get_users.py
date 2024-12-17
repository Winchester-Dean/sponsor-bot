from aiogram.types import Message
from database.db import DataBase
from dispatcher import dp

db = DataBase()

@dp.message_handler(commands=['get_admins'], state="*")
async def get_admins(msg: Message):
    users = db.get_users()

    if not users:
        return await msg.answer("Список администраторов пуст.")
    
    for user in users:
        users_list = "\n".join(
            f"ID: {user[0]}: <a href='https://t.me/user?id={user[0]}'>{admin[1]}</a>"
        )
    
    await msg.answer(f"Список администраторов:\n{admin_list}")

