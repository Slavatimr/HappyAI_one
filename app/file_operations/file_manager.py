from aiogram.types import FSInputFile
from app.main import bot
from aiogram import F


async def download(user_id: int, message_id: int, voice: F.voice) -> str:

    path = f"_temp_files/voice_u{user_id}_m{message_id}.mp3"

    await bot.download(voice, destination=path)
    return path


async def upload(assistant_voice_path: str) -> FSInputFile:
    return FSInputFile(assistant_voice_path)
