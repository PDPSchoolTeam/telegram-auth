import logging
import asyncio
from config import BOT_TOKEN
from aiogram.filters.command import Command, CommandStart
from endpoint import register_user
from aiogram import Bot, Dispatcher
from aiogram.types import Message

bot = Bot(BOT_TOKEN)

dp = Dispatcher()


@dp.message(CommandStart())
async def register_commands(message: Message):
    await register_user(
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name or message.from_user.full_name,
        username=message.from_user.username,
        telegram_id=message.from_user.id,
    )
    await message.answer("Register Successful!")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
