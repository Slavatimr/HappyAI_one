async def create_assistant(assistant_name: str) -> str:
    from app.openai.handlers import client
    assistant = await client.beta.assistants.create(
        name=assistant_name,
        instructions="You are a wise man. Just answer the questions.",
        model="gpt-4o"
    )
    return assistant.id


async def create_thread():
    from app.openai.handlers import client
    thread = await client.beta.threads.create()

    return thread.id
