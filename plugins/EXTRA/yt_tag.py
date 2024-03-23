# (c) @KoshikKumar17
import os
import pyrogram
# from pyrogram import Client as Koshik
from pyrogram import filters, Client
from youtubesearchpython import VideosSearch
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
import YoutubeTags # https://pypi.org/project/youtubetags
from YoutubeTags import videotags
from info import ADMINS, SUPPORT_CHAT_ID, SUPPORT_CHAT_RULES, MOVIE_RULES, UPDATE_CHANNEL_ID, PRINT_ID, GRP_LNK, LOW_SIZE, SUPPORT_CHAT



BTNS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('🙇🏻‍♂️Owner🙇🏻‍♂️', url='https://telegram.me/kinzanoufal')
        ]
    ]
)

@Client.on_message(filters.command("yttags"))
async def yttags(bot, message):
    if not message.reply_to_message:
        return await message.reply_text("**Reply to some Youtube link..🤕, Brother.🙃**")
    if not message.reply_to_message.text:
        return await message.reply_text("**Reply to some Youtube link..🤕, Brother.🙃**")
    link = message.reply_to_message.text
    tags = videotags(link)
    if tags=="":
         await message.reply_text("No Tags Found")
    else:
         await message.reply_text(text=f"**These are the Tags that I Found** \n\n ` {tags} ` \n\n\n **@NASRANI_UPDATE**\n",reply_markup=BTNS)
