import asyncio
import logging
from aiogram import Bot, Dispatcher

from app.config import settings
from app.routers import command, voice
logging.basicConfig(level=logging.INFO)


bot = Bot(token=settings.BOT_TOKEN)


async def main():

    dp = Dispatcher()

    dp.include_routers(command.router,
                       voice.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
