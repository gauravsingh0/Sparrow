from typing import Callable

from YoneRobot import pbot , DRAGONS
from pyrogram.types import Message

from ..helpers.admins import get_administrators



def errors(func: Callable) -> Callable:
    async def decorator(client: pbot, message: Message):
        try:
            return await func(client, message)
        except Exception as e:
            await message.reply(f"{type(e).__name__}: {e}")

    return decorator


def authorized_users_only(func: Callable) -> Callable:
    async def decorator(client: pbot, message: Message):
        if message.from_user.id in DRAGONS :
            return await func(client, message)

        administrators = await get_administrators(message.chat)

        for administrator in administrators:
            if administrator == message.from_user.id:
                return await func(client, message)

    return decorator
