from aiogram import Bot, Dispatcher
import asyncio
from dotenv import dotenv_values

from bot.handlers.bot_commands import router

env_vars = dotenv_values(".env")

api_token = env_vars.get("API_TOKEN")


async def main() -> None:
    token = api_token
    bot = Bot(token=token)
    dp = Dispatcher()

    dp.include_router(router)

    # await bot.delete_webhook()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
