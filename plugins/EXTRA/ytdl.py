from __future__ import unicode_literals

import os, requests, asyncio, math, time, wget
from pyrogram import filters, Client
from pyrogram.types import Message

from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL

from utils import temp
import os
import requests
import aiohttp
import yt_dlp
import asyncio
import math
import time
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import FILE_CHANNEL, FILE_FORWARD, SP
import wget
import aiofiles
from Script import script
from pyrogram import filters, Client, enums
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
import youtube_dl
import requests
from info import ADMINS, SUPPORT_CHAT_ID, SUPPORT_CHAT_RULES, MOVIE_RULES, UPDATE_CHANNEL_ID, PRINT_ID, GRP_LNK, LOW_SIZE, SUPPORT_CHAT

import os
import future
import asyncio
import requests
import wget
import time
import yt_dlp
from urllib.parse import urlparse
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL

from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch
from youtubesearchpython import SearchVideos




# ------------------------------------------------------------------------------- #

def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]


def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None




@Client.on_message(filters.command("song"))
def download_song(client, message):
    query = " ".join(message.command[1:])  
    print(query)
    m = message.reply("**🔍 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 ...**")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

        # Add these lines to define views and channel_name
        views = results[0]["views"]
        channel_name = results[0]["channel"]

    except Exception as e:
        m.edit("**🤖 𝐆𝐢𝐯𝐞 🙃 𝐌𝐮𝐬𝐢𝐜 💿 𝐍𝐚𝐦𝐞 😍\n💞 𝐓𝐨 🔊 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 🥀 𝐒𝐨𝐧𝐠❗**")
        print(str(e))
        return
    m.edit("**👻𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ...**")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("**😈𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ...**")

        message.reply_audio(
            audio_file,
            thumb=thumb_name,
            title=title,
            caption=f"{title}\nRᴇǫᴜᴇsᴛᴇᴅ ʙʏ ➪{message.from_user.mention}\nVɪᴇᴡs➪ {views}\nCʜᴀɴɴᴇʟ➪ {channel_name}",
            duration=dur
        )
        m.delete()
    except Exception as e:
        m.edit(" - An error !!")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


@Client.on_message(filters.command(["video", "mp4"]))
async def vsong(client, message: Message):
    urlissed = get_text(message)
    pablo = await client.send_message(message.chat.id, f"**𝙵𝙸𝙽𝙳𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝚅𝙸𝙳𝙴𝙾** `{urlissed}`")
    if not urlissed:
        return await pablo.edit("Invalid Command Syntax Please Check help Menu To Know More!")     
    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        return await pablo.edit_text(f"**𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝙵𝚊𝚒𝚕𝚎𝚍 𝙿𝚕𝚎𝚊𝚜𝚎 𝚃𝚛𝚢 𝙰𝚐𝚊𝚒𝚗..♥️** \n**Error :** `{str(e)}`")       
    
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"""**𝚃𝙸𝚃𝙻𝙴 :** [{thum}]({mo})\n**𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙱𝚈 :** {message.from_user.mention}"""

    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,        
        reply_to_message_id=message.id 
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)
