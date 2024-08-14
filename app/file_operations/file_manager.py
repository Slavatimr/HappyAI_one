from aiogram.types import FSInputFile
from app.main import bot
from aiogram import F
from os import path


async def download(user_id: int, message_id: int, voice: F.voice) -> str:

    user_voice_path = path.join("app", "_temp_files", f"voice_u{user_id}_m{message_id}.mp3")

    await bot.download(voice, destination=user_voice_path)
    return user_voice_path


async def upload(assistant_voice_path: str) -> FSInputFile:
    return FSInputFile(assistant_voice_path)
