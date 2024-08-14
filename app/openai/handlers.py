from openai import OpenAI

from app.config import settings

client = OpenAI(api_key=settings.OPENAI_TOKEN)


async def speech_to_text(user_voice_path: str) -> str:

    with open(user_voice_path, "rb")as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"
        )
    return transcription.text


async def proceed_query(user_text: str) -> str:
    return ''


async def text_to_speech(assistant_text: str, assistant_voice_path: str) -> str:

    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        input=assistant_text
    ) as response:
        response.stream_to_file(assistant_voice_path)

    return assistant_voice_path
