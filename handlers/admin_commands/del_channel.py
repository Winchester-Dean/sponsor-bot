from aiogram import types
from dispatcher import dp
from database.db import DataBase

@dp.message_handler(commands=["deladmin"])
async def delete_admin(msg: types.Message):
    args = msg.text.split(maxsplit=1)
    admins_list = DataBase().get_admins_list()
    channels_id = DataBase().get_channels_id()
    user_id = msg.from_user.id

    if (user_id,) not in admins_list:
        return await msg.reply(
            "<b>Вы не администратор!</b>"
        )
    
    if len(args) == 2:
        pass
    else:
        return await msg.reply("<b>Error</b>")
    
    if args[1].isdigit():
        channel_id = int(args[1])
        if (channel_id,) in channels_id:
            pass
        else:
            return await msg.reply(
                "<b>Такого канала нету в базе!</b>"
            )
    else:
        return await msg.reply("<b>Invalid id</b>")
    
    try:
        DataBase().del_channel(channel_id)
    except Exception as error:
        await msg.answer(
            "<b>{}</b>".format(error)
        )
    
    await msg.answer(
        "<b>Канал успешно удален!</b>"
    )
