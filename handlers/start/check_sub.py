from database.db import DataBase

async def shecksub(bot, user_id):
    channels_id = DataBase().get_channels_id()
    stats = []

    for channel_id in channels_id:
        for chid in channel_id:
            status = await bot.get_chat_member(
                f"-100{chid}", user_id
            )
            stats.append(status["status"])
    
    if "left" in stats:
        return False
    else:
        return True

