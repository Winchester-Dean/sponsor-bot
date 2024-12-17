async def check_subscription(msg, user_id, channel_id):
    try:
        member = await msg.bot.get_chat_member(
            chat_id=channel_id,
            user_id=user_id
        )
        return member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        return False
