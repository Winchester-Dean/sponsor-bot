from aiogram import types
from dispatcher import dp
from database.db import DataBase

@dp.message_handler(commands=["addchannel"])
async def add_channel(msg: types.Message):
    args = msg.text.split(maxsplit=3)
    admins_list = DataBase().get_admins_list()
    user_id = msg.from_user.id

    if (user_id,) not in admins_list:
        return await msg.reply(
            "<b>Вы не администратор!</b>"
        )

    if len(args) == 4:
        pass
    else:
        return await msg.reply("<b>Error</b>")
    
    if args[1].isdigit():
        channel_id = int(args[1])
    else:
        return await msg.reply("<b>Invalid id</b>")

    try:
        DataBase().new_channel(
            channel_id, args[2], args[3]
        )
    except Exception as error:
        return await msg.answer(
            "<b>{}</b>".format(
                error
            )
        )

    await msg.answer(
        "<b>Новый канал записан в базу!</b>"
    )

