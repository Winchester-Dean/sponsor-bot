import os
from pathlib import Path
from aiogram import types
from aiogram.dispatcher.filters import Text
from dispatcher import dp, bot

from handlers.start.start import check_sub

@dp.message_handler(Text("Android ucin", ignore_case=True))
async def android_code(msg: types.Message):
    try:
        status = await check_sub(bot, msg.from_user.id)
        if status:
            pass
        else:
            return

        directory = "configs/android"
        files = [
            ".nm", ".dark", ".hc", ".npv4"
        ]
        for file in os.listdir(directory):
            if any(file.endswith(ext) for ext in files):
                file_path = os.path.join(f"{directory}/{file}")
                file_name = os.path.basename(file_path)
                with open(file_path, "rb") as f:
                    await bot.send_document(
                        chat_id=msg.chat.id,
                        document=f,
                        caption="BET KOD"
                    )
    except Exception as error:
        await msg.answer(error)


@dp.message_handler(Text("iOS ucin", ignore_case=True))
async def ios_code(msg: types.Message):
    try:
        status = await check_sub(bot, msg.from_user.id)
        if status:
            pass
        else:
            return

        directory = "configs/ios"
        for file in os.listdir(directory):
            if file.endswith(".inpv"):
                with open(f"{directory}/{file}", "rb") as f:
                    await bot.send_document(
                        chat_id=msg.chat.id,
                        document=f,
                        caption="BET KOD"
                    )
    except Exception as error:
        await msg.answer(error)
