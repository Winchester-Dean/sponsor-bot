import os

from aiogram import types
from dispatcher import dp, bot
from aiogram.dispatcher.filters import Text

from handlers.start.keyboards import inline_buttons
from handlers.start.check_sub import checksub

@dp.message_handler(Text("iOS ucin", ignore_case=True))
async def ios_handler(msg: types.Message):
    status = await checksub(bot, msg.from_user.id)
    if status:
        pass
    else:
        return await msg.answer(
            "<b>Siz agza bolmansynyz!</b>",
            reply_markup=inline_buttons
        )
    
    directory_path = os.path.join(
        os.path.dirname(__file__),
        "configs/ios"
    )

    try:
        with open(directory_path, "rb") as file:
            await bot.send_document(
                chat_id = msg.chat.id,
                document=file,
                caption="iOS ucin bet kod"
            )
    except Exception as error:
        await msg.answer(f"<b>{error}</b>")
    
@dp.message_handler(Text("Android ucin", ignore_case=True))
async def android_handler(msg: types.Message):
    status = await checksub(bot, msg.from_user.id)
    if status:
        pass
    else:
        return await msg.answer(
            "<b>Siz agza bolmansynyz!</b>",
            reply_markup=inline_buttons
        )
    
    file_ends = [
        ".nm", ".dark",
        ".npv4", ".hc"
    ]

    directory_path = os.path.join(
        os.path.dirname(__file__),
        "configs/android"
    )

    try:
        for file in os.listdir(directory_path):
            if any(file.endswith(ext) for ext in file_ends):
                with open(directory_path, "rb") as config:
                    await bot.send_document(
                        chat_id=msg.chat.id,
                        document=config,
                        caption="Android ucin bet kod"
                    )
    except Exception as error:
        await msg.answer(f"<b>{error}</b>")
