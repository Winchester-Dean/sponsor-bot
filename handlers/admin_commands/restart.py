import subprocess
import os

from aiogram import types
from dispatcher import dp
from database.db import DataBase

@dp.message_handler(commands=["restart"])
async def restart_handler(msg: types.Message):
    admins_list = DataBase().get_admins_id()
    user_id = msg.from_user.id

    if (user_id,) not in admins_list:
        return await msg.reply(
            "<b>вы не администратор!</b>"
        )
    
    await msg.answer("<b>Перезапуск запущен!</b>")

    process = subprocess.Popen(
        ["ps", "aux"],
        stdout=subprocess.PIPE
    )

    output, error = process.communicate()

    for line in output.decode().split("\n"):
        if "python3" in line and "main.py" in line:
            pid = int(line.split()[1])
            subprocess.run(
                ["kill", str(pid)]
            )
    
    script_path = os.path.join(
        os.path.dirname(__file__),
        "main.py"
    )
    subprocess.Popen(
        [
            "nohup",
            "python3",
            script_path,
            "&"
        ]
    )

    await msg.answer("<b>Бот перезапущен!</b>")
