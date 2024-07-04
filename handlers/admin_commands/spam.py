from aiogram import types
from dispatcher import dp, bot
from database.db import DataBase

@dp.message_handler(commands=["spam"])
async def spam_handler(msg: types.Message):
    args = msg.text.split(maxsplit=1)
    admins_list = DataBase().get_admins_id()
    user_id = msg.from_user.id
    users = DataBase().get_users_id()

    if (user_id,) not in admins_list:
        return await msg.reply("<b>Вы не администратор!</b>")

    if len(args) == 2:
        pass
    else:
        return await msg.reply("<b>Error</b>")

    for user in users:
        try:
            await bot.send_message(
                user[0],
                args[1]
            )
        except:
            continue

    await msg.answer("<b>Рассылка окончена!</b>")
