import asyncio
from aiogram import Bot, Dispatcher
from handlers.dice import rt as dice
dp = Dispatcher()
BOT_TOKEN = "8919352237:AAGjhNV5Joli7RE7Zza0j4VtgGY0bkgTvlQ"
async def main():
    bot = Bot(BOT_TOKEN)

    dp.include_router(dice)

    await dp.start_polling(bot)

if __name__ == "__main__":
        print("start bot")
        asyncio.run(main())
