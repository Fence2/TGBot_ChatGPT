from aiogram import Dispatcher

from telegram_bot.handlers.main_handlers import register_main_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    register_main_handlers(dp)
