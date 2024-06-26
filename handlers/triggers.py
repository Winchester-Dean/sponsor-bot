import os
from aiogram import types
from aiogram.dispatcher.filters import Text
from dispatcher import dp, bot

@dp.message_handler(Text("iOS ucin", ignore_case=True))
async def ios_code(msg: types.Message):
    directory = "configs/ios"
    for file in os.listdir(directory):
        await bot.send_document(
            msg.chat.id,
            f"{directory}/{file}",
            "Bet kod"
        )

@dp.message_handler(Text("Android ucin", ignore_case=True))
async def android_code(msg: types.Message):
    directory = "configs/android"
    for file in os.listdir(directory):
        with open(f"{directory}/{file}", "rb") as f:
            await bot.send_document(
                msg.chat.id,
                f,
                "bet kod"
        )
