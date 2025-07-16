from pyrogram import Client, filters
import os

api_id = int(os.getenv("25960539"))
api_hash = os.getenv("264cc6d76bda37f314bf4349581aa451")
source_channel = os.getenv("stopgameru")  # Пример: "@stopgamenews"
target_channel = os.getenv("@lvlupnws")  # Пример: "@lvlupnws"

app = Client("forwarder", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.chat(source_channel))
async def forward(client, message):
    await message.copy(chat_id=target_channel)

app.run()
