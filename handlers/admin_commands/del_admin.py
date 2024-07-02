from aiogram import types
from dispatcher import dp
from database.db import DataBase

@dp.message_handler(commands=["deladmin"])
async def delete_admin(msg: types.Message):
    args = msg.text.split(maxsplit=1)
    owners = DataBase().get_owners_id()
    admins_list = DataBase().get_admins_id()
    user_id = msg.from_user.id

    if (user_id,) not in owners:
        return await msg.reply(
            "<b>Вы не главный администратор!</b>"
        )

    if len(args) == 2:
        pass
    else:
        return await msg.reply("<b>Error</b>")
    
    if args[1].isdigit():
        admin_id = int(args[1])
        if (admin_id,) in admins_list:
            pass
        else:
            return await msg.reply(
                "<b>Такого администратора нету в базе!</b>"
            )
    else:
        return await msg.reply("<b>Invalid id</b>")

    try:
        DataBase().del_admin(admin_id)
    except Exception as error:
        await msg.answer(
            "<b>{}</b>".format(error)
        )

    await msg.answer(
        "<b>Администратор успешно удалён!</b>"
    )

