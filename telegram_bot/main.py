from aiogram import Bot, Dispatcher, executor

from telegram_bot.utils import Env
from telegram_bot.handlers import register_all_handlers


async def __on_start_up(dp: Dispatcher) -> None:
    register_all_handlers(dp)


def start_telegram_bot() -> None:
    bot = Bot(token=Env.TGBOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot)
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)
