from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from fommbot import pbot as client


Krutika = "https://telegra.ph//file/c8f39f721f967e8e70fc9.jpg"

@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Krutika,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [𝘒 𝘙 𝘜 𝘛 𝘐 𝘒 𝘈🇮🇳](t.me/FULL_ON_MOJ_MASTI)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [🌹 官方 🥀❥͜͡𝄟༎꯭❰᭄ мя zσηєу χ∂ 😈](tg://user?id=5320093001)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**𝘒 𝘙 𝘜 𝘛 𝘐 𝘒 𝘈 ʀᴏʙᴏᴛ sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴅᴇᴠᴇʟᴏᴘᴇʀ •", url="tg://user?id=5218610039"), 
                    InlineKeyboardButton(
                        "• sᴏᴜʀᴄᴇ •", url="https://github.com/Chiranjibkoch/fommbot")
                ]
            ]
        )
    )

__mod_name__ = "Rᴇᴩᴏ"
