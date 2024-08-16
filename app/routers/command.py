from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command('start'))
async def start(message: Message):
    await message.answer(text="Привет, я могу ответить тебе почти на любой вопрос. "
                              "Просто отправь мне голосовое сообщение.")
