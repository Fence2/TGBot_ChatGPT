import logging
import time
from aiogram import Dispatcher, Bot
from aiogram.types import Message
from .ChatGPT import get_chatgpt_answer


async def start_handler(msg: Message) -> None:
    user_id = msg.from_user.id
    user_full_name = msg.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

    await msg.answer(f"Привет, {user_full_name}")


async def get_help(msg: Message) -> None:
    bot: Bot = msg.bot
    help_message = (
        "Доступные команды:\n"
        "/id - получение вашего Telegram ID\n"
        "/chagpt \"вопрос\" - Задать вопрос ИИ: ChatGPT"
    )
    await bot.send_message(msg.from_user.id, help_message)


async def get_full_msg(msg: Message) -> None:
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, str(msg))


async def other_messages(msg: Message) -> None:
    bot: Bot = msg.bot
    await bot.send_message(msg.from_user.id, "Я вас не понял, напишите /start!")


async def __get_id(msg: Message) -> None:
    bot: Bot = msg.bot
    user = msg.from_user
    await bot.send_message(user.id, f"{user.username}: <code>{user.id}</code>")


def register_main_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(get_full_msg, commands=['get_full_msg'])
    dp.register_message_handler(get_help, commands=['help'])
    dp.register_message_handler(get_chatgpt_answer, commands=['chatgpt'])
    dp.register_message_handler(__get_id, commands=["id"])
    dp.register_message_handler(other_messages, content_types=['text'], state=None)
