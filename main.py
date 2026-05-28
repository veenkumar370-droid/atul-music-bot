import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

BOT_NAME = "ATUL MUSIC"
OWNER = "Atul Tech Care"

bot = Client(
    "atul_music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start(client, message: Message):
    name = message.from_user.first_name

    text = f"👋 Hello {name}!\n\n🎵 Welcome to {BOT_NAME}\n\n📺 YouTube: Atul Tech Care"

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("📺 YouTube", url="https://youtube.com/@AtulTechCare")]
    ])

    await message.reply_text(text, reply_markup=buttons)

print("Bot Started 🔥")
bot.run()
