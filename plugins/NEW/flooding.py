import os

import logging
logger = logging.getLogger(__name__)
import os, re, time, math, json, string, random, traceback, wget, asyncio, datetime, aiofiles, aiofiles.os, requests, youtube_dl, wget

from random import choice 
from pyrogram import Client, filters, enums
from pyrogram import Client as Bot
from youtube_search import YoutubeSearch
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid
from info import *


import asyncio
import math
import os
import re
import time

from random import randint
from urllib.parse import urlparse

import aiofiles
import aiohttp
import requests
import wget
import youtube_dl
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos



UPDATES_CHANNEL = LOG_CHANNEL

import os
import logging
import pyrogram









#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os
import asyncio
from urllib.parse import urlparse
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from youtube_dl import YoutubeDL
# from opencc import * # OpenCC
import wget

SUPPORT = LOG_CHANNEL





if __name__ == "__main__" :
    plugins = dict(
        root="mt_privateautocaption"
    )
    Bot = pyrogram.Client(
        "CaptionBot",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins,
        workers=300
    )
    

    
AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "No")

VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "No")

# db = Database()

START_TEXT = """ `Hai {}, 
Am a YouTube Downloader Bot I Can Download Songs,Videos and Lyrics From YouTube and lyrics and  Would upload into Telegram. 
Use /help Commands For More.`
"""

CMDS_TEXT = """
`Here It is The List of Commamds and Its usage.`

- /song - This Command is For Downloading Songs. 
- /lyrics - This Command is For Scrapping Lyrics of a Song. 
- /video - This Command is For Downloading Videos. 
- Also You Can search videos via inline Mode on Bot. 

`Exmples For Both Those Commands.`

- /song [song name] or [youTube link]. 
  [/song Alone]. 
- /lyrics [song name]. 
  [/lyrics alone] 
- /video [video name] or [YouTube link] 
  [/video Alone] 
  
"""

ABOUT_TEXT = """
- **Bot :** `Song Downloader`
- **Creator :** [MR-JINN-OF-TG](https://Github.com/MR-JINN-OF-TG)
- **Support :** [CLICK HERE](https://telegram.me/NAZRIYASUPPORT)
- **Source :** [CLICK HERE](https://github.com/MR-JINN-OF-TG/Song-Downloader)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram](https://pyrogram.org)
- **Server :** [Heroku](https://heroku.com)

"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Support📕', url=f"https://telegram.me/{SUPPORT}"), 
        InlineKeyboardButton(text="SEARCH🔎", switch_inline_query_current_chat="")
        ],[
        InlineKeyboardButton('HELP & USAGE⚙️', callback_data ='cmds') 
        ],[
        InlineKeyboardButton('ABOUT📕', callback_data='about'),
        InlineKeyboardButton('CLOSE🔐', callback_data='close')
        ]]
    )
CMDS_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('HOME🏡', callback_data='home'),
        InlineKeyboardButton('CLOSE🔐', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('HOME🏡', callback_data='home'),
        InlineKeyboardButton('CLOSE🔐', callback_data='close')
        ]]
    )

@Bot.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "cmds":
        await update.message.edit_text(
            text=CMDS_TEXT,
            reply_markup=CMDS_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()











YTDL_REGEX = (r"^((?:https?:)?\/\/)"
              r"?((?:www|m)\.)"
              r"?((?:youtube\.com|youtu\.be|xvideos\.com|pornhub\.com"
              r"|xhamster\.com|xnxx\.com))"
              r"(\/)([-a-zA-Z0-9()@:%_\+.~#?&//=]*)([\w\-]+)(\S+)?$")



@Bot.on_message(filters.private
                   & filters.text
                   & filters.regex(YTDL_REGEX))
async def ytdl_with_button(c: Client, message: Message):
    if UPDATES_CHANNEL is not None:
        try:
            user = await c.get_chat_member(UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=message.chat.id,
                    text="Sorry, You are Banned to use me. Contact my [master](https://t.me/ZauteBot).",
                    parse_mode=enums.ParseMode.MARKDOWN,
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await c.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use me 😉**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/{UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode=enums.ParseMode.MARKDOWN
            )
            return
        except Exception:
            await c.send_message(
                chat_id=message.chat.id,
                text="Something went Wrong. Contact my [master](https://t.me/zautebot).",
                parse_mode=enums.ParseMode.MARKDOWN,
                disable_web_page_preview=True)
            return
    await message.reply_text(
        "**Choose Download type👇**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎵 Audio",
                        callback_data="ytdl_audio"
                    ),
                    InlineKeyboardButton(
                        "Video 🎬",
                        callback_data="ytdl_video"
                    )
                ]
            ]
        ),
        quote=True
    )

@Client.on_callback_query(filters.regex(r"^ytdl_audio$"))
# @Bot.on_callback_query(filters.regex("^ytdl_audio$"))
async def callback_query_ytdl_audio(_, callback_query):
    try:
        url = callback_query.message.reply_to_message.text
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': '%(title)s - %(extractor)s-%(id)s.%(ext)s',
            'writethumbnail': True
        }
        with YoutubeDL(ydl_opts) as ydl:
            message = callback_query.message
            k = await callback_query.message.reply_text(f"okkkk")
#            await message.reply_chat_action("typing")
            info_dict = ydl.extract_info(url, download=False)
            # download
            await callback_query.message.edit_text("**Downloading audio...**")
            ydl.process_info(info_dict)
            # upload
            audio_file = ydl.prepare_filename(info_dict)
            task = asyncio.create_task(send_audio(message, info_dict,
                                                  audio_file))
            while not task.done():
                await asyncio.sleep(3)
            await message.delete()
    except Exception as e:
        await message.reply_text(e)
    await callback_query.message.reply_to_message.delete()
    await callback_query.message.delete()


if AUDIO_THUMBNAIL == "No":
   async def send_audio(message: Message, info_dict, audio_file):
       basename = audio_file.rsplit(".", 1)[-2]
       # .webm -> .weba
       if info_dict['ext'] == 'webm':
           audio_file_weba = basename + ".weba"
           os.rename(audio_file, audio_file_weba)
           audio_file = audio_file_weba
       # thumbnail
       thumbnail_url = info_dict['thumbnail']
       thumbnail_file = basename + "." + \
           get_file_extension_from_url(thumbnail_url)
       # info (s2tw)
       webpage_url = info_dict['webpage_url']
       title = s2tw(info_dict['title'])
       caption = f"<b><a href=\"{webpage_url}\">{title}</a></b>"
       duration = int(float(info_dict['duration']))
       performer = s2tw(info_dict['uploader'])
       await message.reply_audio(audio_file, caption=caption, duration=duration,
                              performer=performer, title=title,
                              parse_mode=enums.ParseMode.HTML, thumb=thumbnail_file)
       os.remove(audio_file)
       os.remove(thumbnail_file)

else:
    async def send_audio(message: Message, info_dict, audio_file):
       basename = audio_file.rsplit(".", 1)[-2]
       # .webm -> .weba
       if info_dict['ext'] == 'webm':
           audio_file_weba = basename + ".weba"
           os.rename(audio_file, audio_file_weba)
           audio_file = audio_file_weba
       # thumbnail
       lol = AUDIO_THUMBNAIL
       thumbnail_file = wget.download(lol)
       # info (s2tw)
       webpage_url = info_dict['webpage_url']
       title = s2tw(info_dict['title'])
       caption = f"<b><a href=\"{webpage_url}\">{title}</a></b>"
       duration = int(float(info_dict['duration']))
#       performer = s2tw(info_dict['uploader'])
       await message.reply_audio(audio_file, caption=caption, duration=duration,
                              title=title,
                              parse_mode=enums.ParseMode.HTML, thumb=thumbnail_file)
       os.remove(audio_file)
       os.remove(thumbnail_file)




def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]


def get_resolution(info_dict):
    if {"width", "height"} <= info_dict.keys():
        width = int(info_dict['width'])
        height = int(info_dict['height'])
    # https://support.google.com/youtube/answer/6375112
    elif info_dict['height'] == 1080:
        width = 1920
        height = 1080
    elif info_dict['height'] == 720:
        width = 1280
        height = 720
    elif info_dict['height'] == 480:
        width = 854
        height = 480
    elif info_dict['height'] == 360:
        width = 640
        height = 360
    elif info_dict['height'] == 240:
        width = 426
        height = 240
    return (width, height)
