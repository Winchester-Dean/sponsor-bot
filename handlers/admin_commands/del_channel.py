from aiogram import types
from dispatcher import dp
from database.db import DataBase

@dp.message_handler(commands=["delchannel"])
async def delete_channel(msg: types.Message):
    args = msg.text.split(maxsplit=1)
    admins_list = DataBase().get_admins_id()
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
        if (channel_id,) not in channels_id:
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
