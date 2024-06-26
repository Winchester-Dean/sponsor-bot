import os
from aiogram import types
from dispatcher import dp, bot

@dp.message_handler(Text("iOS ucin", ignore_case=True))
async def ios_code(msg: types.Message):
    directory = "configs/ios"
    for file in os.listdir(directory):
        await bot.send_document(
            msg.chat.id,
            file,
            "Bet kod"
        )

@dp.message_handler(Text("Android ucin", ignore_case=True))
async def android_code(msg: types.Message):
    directory = "configs/android"
    for file in os.listdir(directory):
        await bot.send_document(
            msg.chat.id,
            file,
            "bet kod"
        )
