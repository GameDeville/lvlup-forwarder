from pyrogram import Client, filters
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
source_channel = os.getenv("SOURCE_CHANNEL")  # Пример: "@stopgamenews"
target_channel = os.getenv("TARGET_CHANNEL")  # Пример: "@lvlupnws"

app = Client("forwarder", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.chat(source_channel))
async def forward(client, message):
    await message.copy(chat_id=target_channel)

app.run()
