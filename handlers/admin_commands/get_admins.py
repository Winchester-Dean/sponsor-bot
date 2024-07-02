from aiogram import types
from dispatcher import dp
from database.db import DataBase

@dp.message_handler(commands=["getadmins"])
async def get_admins_list(msg: types.Message):
    admins_list = DataBase().get_admins_id()
    user_id = msg.from_user.id

    if (user_id,) not in admins_list:
        return await msg.reply(
            "<b>Вы не администратор!</b>"
        )

    text = (
        "<b>Admins list:\n</b>"
    )

    admins = DataBase().get_admins()
    for admin in admins:
        dbid = admin[0]
        admin_id = admin[1]
        name = admin[2]
        
        text += "{}. <a href='tg://user?id={}'>{}</a>: <code>{}</code>\n".format(
            dbid, admin_id, name, admin_id
        )

    await msg.answer(text)

