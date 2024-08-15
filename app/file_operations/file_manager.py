import json
from typing import Optional
from os import path

import aiofiles
from aiogram.types import FSInputFile
from aiogram import F

from app.main import bot
from app.openai.assistants_and_threads_creation import create_thread, create_assistant


async def download(user_id: int, message_id: int, voice: F.voice) -> str:

    user_voice_path = path.join("app", "_temp_files", f"voice_u{user_id}_m{message_id}.mp3")

    await bot.download(voice, destination=user_voice_path)
    return user_voice_path


async def upload(assistant_voice_path: str) -> FSInputFile:

    return FSInputFile(assistant_voice_path)


async def get_json_dict(filename: str):

    filename = path.join("fake_db", f"{filename}.json")

    async with aiofiles.open(file=filename, mode="r", encoding="utf-8") as file:
        json_file = await file.read()

    return json.loads(json_file)


async def get_from_json(filename: str, chat_id: Optional[str] = "", assistant_name: Optional[str] = ""):

    try:
        json_dict = await get_json_dict(filename=filename)
        result_id = json_dict[chat_id + assistant_name]
        return result_id

    except KeyError:

        if "threads" == filename:
            result_id = await create_thread()
            await post_to_json(key=chat_id, value=result_id, filename="threads")
            return result_id

        elif "assistants" == filename:
            result_id = await create_assistant(assistant_name=assistant_name)
            await post_to_json(key=assistant_name, value=result_id, filename="assistants")
            return result_id


async def post_to_json(key: str, value: str, filename: str):

    json_dict = await get_json_dict(filename=filename)
    json_dict[key] = value

    async with aiofiles.open(file=path.join("fake_db", f"{filename}.json"),
                             mode='w',
                             encoding='utf-8') as file:
        await file.write(json.dumps(json_dict, ensure_ascii=False, indent=4))
