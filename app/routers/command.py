from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command('start'))
async def start(message: Message):
    await message.answer(text="Ура! Я закончил, годная задача, мне понравилась. Все довольно просто, "
                              "но документация не самая понятная у опенэйай. Пожалуй, напишу статью на хабр.")
