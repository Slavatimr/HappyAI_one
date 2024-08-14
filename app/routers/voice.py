import os

from aiogram import Router, F
from aiogram.methods import SendVoice
from aiogram.types import Message

from app.file_operations.file_manager import download, upload
from app.openai.handlers import speech_to_text, text_to_speech, proceed_query

router = Router()


@router.message(F.voice)
async def start(message: Message):

    user_voice_path = await download(user_id=message.from_user.id,
                                     message_id=message.message_id,
                                     voice=message.voice)

    user_text = await speech_to_text(user_voice_path)
    await message.answer(user_text)
    os.remove(user_voice_path)
'''
    assistant_text = await proceed_query(user_text)

    assistant_voice_path = await text_to_speech(assistant_text, user_voice_path)

    file = await upload(assistant_voice_path)
    os.remove(assistant_voice_path)
    return SendVoice(chat_id=message.chat.id, voice=file)'''
