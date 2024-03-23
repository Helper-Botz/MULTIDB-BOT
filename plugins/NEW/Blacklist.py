"""

COPY KARLO FUCKING BITCHES

"""
import re
from datetime import datetime, timedelta

from pyrogram import filters, Client, enums
from pyrogram.types import ChatPermissions
from pyrogram.errors import ChatAdminRequired


# from AarohiX.utils.errors import capture_err

from motor.motor_asyncio import AsyncIOMotorClient

from typing import List
from info import SECOND_URI, SECOND_NAME, ADMINS, LOG_CHANNEL

import logging


from time import time
from functools import wraps
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import ChannelPrivate, ChatWriteForbidden, UserNotParticipant
from pyrogram.raw import functions
from pyrogram.raw.types import InputChannelEmpty, InputPeerChannel
from pyrogram.types import ChatPermissions, ChatMember, User
from pyrogram import enums

import os
import traceback
from datetime import datetime
from functools import wraps

from pyrogram.errors.exceptions.forbidden_403 import ChatWriteForbidden
from pyrogram.types import CallbackQuery




def capture_err(func):
    @wraps(func)
    async def capture(client, message, *args, **kwargs):
        if isinstance(message, CallbackQuery):
            sender = message.message.reply
            chat = message.message.chat
            msg = message.message.text or message.message.caption
        else:
            sender = message.reply
            chat = message.chat
            msg = message.text or message.caption
        try:
            return await func(client, message, *args, **kwargs)
        except ChatWriteForbidden:
            return await client.leave_chat(message.chat.id)
        except Exception as err:
            exc = traceback.format_exc()
            error_feedback = "ERROR | {} | {}\n\n{}\n\n{}\n".format(
                message.from_user.id if message.from_user else 0,
                chat.id if chat else 0,
                msg,
                exc,
            )
            day = datetime.now()
            tgl_now = datetime.now()

            cap_day = f"{day.strftime('%A')}, {tgl_now.strftime('%d %B %Y %H:%M:%S')}"
            await sender(
                "😭 An Internal Error Occurred while processing your Command, the Logs have been sent to the Owners of this Bot. Sorry for Inconvenience..."
            )
            with open(
                f"crash_{tgl_now.strftime('%d %B %Y')}.txt", "w+", encoding="utf-8"
            ) as log:
                log.write(error_feedback)
                log.close()
            await client.send_document(
                LOG_CHANNEL,
                f"crash_{tgl_now.strftime('%d %B %Y')}.txt",
                caption=f"Crash Report of this Bot\n{cap_day}",
            )
            os.remove(f"crash_{tgl_now.strftime('%d %B %Y')}.txt")
            raise err

    return capture


# Assuming admins_in_chat is a global variable defined somewhere in your code
admins_in_chat = {}

async def authorised(func, subFunc2, client, message, *args, **kwargs):
    try:
        await func(client, message, *args, **kwargs)
    except ChatWriteForbidden:
        await message.chat.leave()
    except Exception as e:
        try:
            await message.reply_text(str(e))
        except AttributeError:
            await message.reply_text("An error occurred.")
        print(f"Error in authorised: {e}")
    return subFunc2



async def member_permissions(chat_id: int, user_id: int, app: Client):
    perms = []
    try:
        member = await app.get_chat_member(chat_id, user_id)
        if member.status == "member":
            if member.can_post_messages:
                perms.append("can_post_messages")
            if member.can_edit_messages:
                perms.append("can_edit_messages")
            if member.can_delete_messages:
                perms.append("can_delete_messages")
            if member.can_restrict_members:
                perms.append("can_restrict_members")
            if member.can_promote_members:
                perms.append("can_promote_members")
            if member.can_change_info:
                perms.append("can_change_info")
            if member.can_invite_users:
                perms.append("can_invite_users")
            if member.can_pin_messages:
                perms.append("can_pin_messages")
            if member.can_manage_video_chats:
                perms.append("can_manage_video_chats")
        return perms
    except UserNotParticipant:
        # Handle the case when the user is not a participant in the chat
        return []
    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error in member_permissions: {e}")
        return []

async def unauthorised(message: Message, permission, subFunc2):
    text = f"You don't have the required permission to perform this action.\n**Permission:** __{permission}__"
    try:
        await message.reply_text(text)
    except ChatWriteForbidden:
        await message.chat.leave()
    return subFunc2


# Update the list_admins function
async def list_admins(chat_id: int, client: Client):
    if chat_id in admins_in_chat:
        interval = time() - admins_in_chat[chat_id]["last_updated_at"]
        if interval < 3600:
            return admins_in_chat[chat_id]["data"]

    try:
        admins_in_chat[chat_id] = {
            "last_updated_at": time(),
            "data": [
                member.user.id
                async for member in client.get_chat_members(
                    chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS
                )
            ],
        }
        return admins_in_chat[chat_id]["data"]
    except ChannelPrivate:
        return


def adminsOnly(permission):
    def subFunc(func):
        @wraps(func)
        async def subFunc2(client, message: Message, *args, **kwargs):
            chatID = message.chat.id
            if not message.from_user:
                # For anonymous admins
                if message.sender_chat and message.sender_chat.id == message.chat.id:
                    return await authorised(
                        func,
                        subFunc2,
                        client,
                        message,
                        *args,
                        **kwargs,
                    )
                return await unauthorised(message, permission, subFunc2)
            # For admins and sudo users
            userID = message.from_user.id
            permissions = await member_permissions(chatID, userID, client)
            if userID not in ADMINS and permission not in permissions:
                return await unauthorised(message, permission, subFunc2)
            return await authorised(func, subFunc2, client, message, *args, **kwargs)

        return subFunc2

    return subFunc


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


client = AsyncIOMotorClient(SECOND_URI)
mongodb = client[SECOND_NAME]





blacklist_filtersdb = mongodb["blacklistFilters"]

async def get_blacklisted_words(chat_id: int) -> List[str]:
    _filters = await blacklist_filtersdb.find_one({"chat_id": chat_id})
    return [] if not _filters else _filters["filters"]

async def save_blacklist_filter(chat_id: int, word: str):
    word = word.lower().strip()
    _filters = await get_blacklisted_words(chat_id)
    _filters.append(word)
    await blacklist_filtersdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"filters": _filters}},
        upsert=True,
    )

async def delete_blacklist_filter(chat_id: int, word: str) -> bool:
    filtersd = await get_blacklisted_words(chat_id)
    word = word.lower().strip()
    if word in filtersd:
        filtersd.remove(word)
        await blacklist_filtersdb.update_one(
            {"chat_id": chat_id},
            {"$set": {"filters": filtersd}},
            upsert=True,
        )
        return True
    return False




__MODULE__ = "Blacklist"
__HELP__ = """
/blacklisted - Get All The Blacklisted Words In The Chat.
/blacklist [WORD|SENTENCE] - Blacklist A Word Or A Sentence.
/whitelist [WORD|SENTENCE] - Whitelist A Word Or A Sentence.
"""


@Client.on_message(filters.command("blacklist") & ~filters.private)
@adminsOnly("can_restrict_members")
async def save_filters(_, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage:\n/blacklist [WORD|SENTENCE]")
    word = message.text.split(None, 1)[1].strip()
    if not word:
        return await message.reply_text("**Usage**\n__/blacklist [WORD|SENTENCE]__")
    chat_id = message.chat.id
    await save_blacklist_filter(chat_id, word)
    await message.reply_text(f"__**Blacklisted {word}.**__")


@Client.on_message(filters.command("blacklisted") & ~filters.private)
@capture_err
async def get_filterss(_, message):
    data = await get_blacklisted_words(message.chat.id)
    if not data:
        await message.reply_text("**No blacklisted words in this chat.**")
    else:
        msg = f"List of blacklisted words in {message.chat.title} :\n"
        for word in data:
            msg += f"**-** `{word}`\n"
        await message.reply_text(msg)


@Client.on_message(filters.command("whitelist") & ~filters.private)
@adminsOnly("can_restrict_members")
async def del_filter(_, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage:\n/whitelist [WORD|SENTENCE]")
    word = message.text.split(None, 1)[1].strip()
    if not word:
        return await message.reply_text("Usage:\n/whitelist [WORD|SENTENCE]")
    chat_id = message.chat.id
    deleted = await delete_blacklist_filter(chat_id, word)
    if deleted:
        return await message.reply_text(f"**Whitelisted {word}.**")
    await message.reply_text("**No such blacklist filter.**")


# ... (previous code)

@Client.on_message(filters.text & ~filters.private, group=8)
@capture_err
async def blacklist_filters_re(client, message):  # Added 'client' argument
    text = message.text.lower().strip()
    if not text:
        return
    chat_id = message.chat.id
    user = message.from_user
    if not user:
        return
    if user.id in ADMINS:
        return
    list_of_filters = await get_blacklisted_words(chat_id)
    
    # Pass 'client' to list_admins function
    if user.id in await list_admins(chat_id, client=client):
        return
    
    for word in list_of_filters:
        pattern = r"( |^|[^\w])" + re.escape(word) + r"( |$|[^\w])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            try:
                await message.delete()
                await message.chat.restrict_member(
                    user.id,
                    ChatPermissions(all_perms=False),
                    until_date=datetime.now() + timedelta(hours=1),
                )
            except ChatAdminRequired:
                return await message.reply("Please give me admin permissions to blacklist user", quote=False)
            except Exception as err:
                print(f"ERROR Blacklist Chat: ID = {chat_id}, ERR = {err}")
                return
            await app.send_message(
                chat_id,
                f"Muted {user.mention} [`{user.id}`] for 1 hour "
                + f"due to a blacklist match on {word}.",
            )


"""
Copyright (c) 2024 @dil_sagar_121
Copyright (c) 2024 @Alone_Dil_bot
"""
