import os
from aiogram import types
from dispatcher import dp, bot

@dp.message_handler(Text("Android ucin", ignore_case=True))
async def android_code(msg: types.Message):
    directory = "configs/android"
    files = [
        ".nm", ".dark", ".hc", ".npv4"
    ]

    for file in os.listdir(directory):
        for ends in files:
            if file.endswith(ends):
                with open(f"{directory}/{file}", "rb") as f:
                    if os.path.getsize(f"{directory}/{file}") > 0:
                        await bot.send_document(
                            chat_id=msg.chat.id,
                            document=f
                        )

@dp.message_handler(Text("iOS ucin", ignore_case=True))
async def ios_code(msg: types.Message):
    directory = "configs/ios"
    for file in os.listdir(directory):
        if file.endswith(".inpv"):
            with open(f"{directory}/{file}") as f:
                if os.path.getsize(f"{directory}/{file}") > 0:
                    await bot.send_document(
                        chat_id=msg.chat.id,
                        document=f
                    )
