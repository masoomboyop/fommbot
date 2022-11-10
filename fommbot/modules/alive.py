import random
from pyrogram import __version__ as pyrover
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from fommbot import OWNER_USERNAME, SUPPORT_CHAT, dispatcher
from fommbot.events import register
from fommbot import telethn as tbot


PHOTO = [
    "https://telegra.ph//file/68b68eee6396bfcfd4b2c.jpg",
    "https://telegra.ph//file/59999e8314c89af585276.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ ᴋʀᴜᴛɪᴋᴀ**\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [𝘒 𝘙 𝘜 𝘛 𝘐 𝘒 𝘈](https://t.me/Krutika_X_BOT)** \n\n"
  TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", f"https://t.me/Krutika_X_BOT?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", f"https://t.me/FULL_ON_MOJ_MASTI"),
        ]
    ]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)
  
 