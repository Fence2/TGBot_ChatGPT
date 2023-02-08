from aiogram import Bot
from aiogram.types import Message
from telegram_bot.utils.env import Env
from revChatGPT import Official

gpt = Official.Chatbot(api_key=Env.OPENAI_TOKEN)

admins = [
    'Fence_2',
]

friends = [
    'nickpositive',
    'Jeingo',
    'Muuuuuuurmuuuuuur',
    'findmay',
    'nickpositive',
    'ArNiFeo',
]

from_work = [
    'liza_veber',
    'kapitanbanan',
    'afrolenkov',
    'mufickthezz',
]


async def get_chatgpt_answer(msg: Message) -> None:
    bot: Bot = msg.bot
    user_username = msg.from_user.username
    good_users = admins + friends + from_work

    if user_username not in good_users:
        await msg.answer(f"Нет прав на выполнение данной команды!")
        return

    user_question = msg.get_args()
    if len(user_question.strip()) == 0:
        await msg.answer(f"Вы не задали вопрос! Используйте команду в таком виде: /chatgpt Ваш вопрос")
        return

    await msg.answer(f"Задаем вопрос ChatGPT. Ответ придет не сразу! Ожидайте, пожалуйста")
    try:
        answer = gpt.ask(user_question)
        for ch in answer['choices']:
            await bot.send_message(msg.from_user.id, ch['text'])
    except Exception as e:
        await bot.send_message(
            msg.from_user.id,
            f"❗Ошибка выполнения запроса❗\n\n<u>{str(e)}</u>"
        )
