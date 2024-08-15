import asyncio

from openai import AsyncOpenAI

from app.config import settings
from app.file_operations.file_manager import get_from_json

client = AsyncOpenAI(api_key=settings.OPENAI_TOKEN)


async def speech_to_text(user_voice_path: str) -> str:

    with open(user_voice_path, "rb") as audio_file:
        transcription = await client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
        )
    return transcription.text


async def proceed_query(user_text: str, chat_id: str) -> str:

    assistant_id = await get_from_json(filename="assistants", assistant_name="Viachaslau")
    thread_id = await get_from_json(filename="threads", chat_id=chat_id)

    await client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_text
    )

    run = await client.beta.threads.runs.create_and_poll(
        thread_id=thread_id,
        assistant_id=assistant_id
    )

    while run.status == "queued" or run.status == "in_progress":
        await asyncio.sleep(0.1)

    messages = await client.beta.threads.messages.list(thread_id=thread_id    )
    return messages.data[0].content[0].text.value


async def text_to_speech(assistant_text: str, assistant_voice_path: str) -> str:

    async with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        input=assistant_text
    ) as response:
        await response.stream_to_file(assistant_voice_path)

    return assistant_voice_path
