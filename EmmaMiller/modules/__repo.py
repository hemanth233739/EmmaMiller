import os
from pyrogram import Client, filters
from pyrogram.types import *

from EmmaMiller.config import get_str_key
from EmmaMiller import pbot

REPO_TEXT = "**A Powerful [BOT](https://telegra.ph/file/012ca899d61231500b90d.jpg) to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 [Mukesh Solanki](https://t.me/mkspali) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @BotMasterOfficial «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("💠 Repository 💠", url=f"https://github.com/BotMasterOfficial/EmmaMiller"),
        InlineKeyboardButton("💠 Join 💠", url=f"https://t.me/RMCMG"),
      ],[
        InlineKeyboardButton("💠 Bot Master 💠", url="https://t.me/BotMaster_mkspali"),
        InlineKeyboardButton("💠 Support 💠", url="https://t.me/BotMasterOfficial"),
      ],[
        InlineKeyboardButton("💠 Emma Updats 💠", url="https://t.me/BotMasterOfficial"),
        InlineKeyboardButton("💠 Developer 💠", url="https://t.me/mkspali"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
