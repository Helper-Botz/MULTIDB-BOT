from pyrogram.types import Message
from pyrogram import filters, Client, enums
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ChatPermissions
)
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    UserAdminInvalid,
    BadRequest
)

import datetime

import logging
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode, ChatType
from info import *


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


async def admin_check(message: Message) -> bool:
    if not message.from_user:
        return False

    if message.chat.type not in [ChatType.SUPERGROUP, ChatType.CHANNEL]:
        return False

    if message.from_user.id in [
        777000,  # Telegram Service Notifications
        1291970954,  # GroupAnonymousBot
    ]:
        return True

    client = message._client
    chat_id = message.chat.id
    user_id = message.from_user.id

    check_status = await client.get_chat_member(chat_id=chat_id, user_id=user_id)
    if check_status.status not in [
        ChatMemberStatus.OWNER,
        ChatMemberStatus.ADMINISTRATOR
    ]:
        return False
    else:
        return True


async def admin_filter_f(filt, client, message):
    return (
        # t, lt, fl 2013
        not message.edit_date
        and await admin_check(message)
    )


admin_filter = filters.create(func=admin_filter_f, name="AdminFilter")


def mention(user, name, mention=True):
    if mention == True:
        link = f"[{name}](tg://openmessage?user_id={user})"
    else:
        link = f"[{name}](https://t.me/{user})"
    return link



async def get_userid_from_username(client, username):
    try:
        user = await client.get_users(username)
    except:
        return None
    
    user_obj = [user.id, user.first_name]
    return user_obj


async def ban_user(client, user_id, first_name, admin_id, admin_name, chat_id, reason, time=None):
    try:
        await client.ban_chat_member(chat_id, user_id)
    except ChatAdminRequired:
        msg_text = "Ban rights? Nah, I'm just here for the digital high-fives 🙌\nGive me ban rights! 😡🥺"
        return msg_text, False
    except UserAdminInvalid:
        msg_text = "I wont ban an admin bruh!!"
        return msg_text, False
    except Exception as e:
        if user_id == 1291970954:
            msg_text = "why should i ban myself? sorry but I'm not stupid like you"
            return msg_text, False
        
        msg_text = f"opps!!\n{e}"
        return msg_text, False

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)
    msg_text = f"{user_mention} was banned by {admin_mention}\n\n reason:- {reason} \n time:- {time}"    
    return msg_text, True


async def unban_user(client, user_id, first_name, admin_id, admin_name, chat_id):
    try:
        await client.unban_chat_member(chat_id, user_id)
    except ChatAdminRequired:
        msg_text = "Ban rights? Nah, I'm just here for the digital high-fives 🙌\nGive me ban rights! 😡🥺"
        return msg_text
    except Exception as e:
        msg_text = f"opps!!\n{e}"
        return msg_text

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)
    
    msg_text = f"{user_mention} was unbanned by {admin_mention}"
    return msg_text



async def mute_user(client, user_id, first_name, admin_id, admin_name, chat_id, reason, time=None):
#    reason = None
    try:
        if time:
            mute_end_time = datetime.datetime.now() + time
            await client.restrict_chat_member(chat_id, user_id, ChatPermissions(), mute_end_time)
        else:
            await client.restrict_chat_member(chat_id, user_id, ChatPermissions())
    except ChatAdminRequired:
        msg_text = "Mute rights? Nah, I'm just here for the digital high-fives 🙌\nGive me mute rights! 😡🥺"
        return msg_text, False
    except UserAdminInvalid:
        msg_text = "I wont mute an admin bruh!!"
        return msg_text, False
    except Exception as e:
        if user_id == 1291970954:
            msg_text = "why should i mute myself? sorry but I'm not stupid like you"
            return msg_text, False
        
        msg_text = f"opps!!\n{e}"
        return msg_text, False

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)

    msg_text = f"{user_mention} was muted by {admin_mention} \n\n reason:- {reason} \n time:- {time}"
    if time:
        
        msg_text += f"time {time}"

    return msg_text, True


async def unmute_user(client, user_id, first_name, admin_id, admin_name, chat_id):
    try:
        await client.restrict_chat_member(
            chat_id,
            user_id,
            ChatPermissions(
                can_send_media_messages=True,
                can_send_messages=True,
                can_send_other_messages=True,
                can_send_polls=True,
                can_add_web_page_previews=True,
                can_invite_users=True
            )
        )
    except ChatAdminRequired:
        msg_text = "Mute rights? Nah, I'm just here for the digital high-fives 🙌\nGive me unmute rights! 😡🥺"
        return msg_text
    except Exception as e:
        msg_text = f"opps!!\n{e}"
        return msg_text

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)
    
    msg_text = f"{user_mention} was unmuted by {admin_mention}"
    return msg_text
    


@Client.on_message(filters.command(["bans"]))
async def ban_command_handler(client, message):
    reason = "okda"
    chat = message.chat
    chat_id = message.chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_restrict_members:
            pass
        else:
            msg_text = "You dont have permission to ban someone"
            return await message.reply_text(msg_text)
    else:
        msg_text = "You dont have permission to ban someone"
        return await message.reply_text(msg_text)

    # Extract the user ID from the command or reply
    if len(message.command) > 1:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            first_name = message.reply_to_message.from_user.first_name
            reason = message.text.split(None, 1)[1]
        else:
            try:
                user_id = int(message.command[1])
                first_name = "User"
            except:
                user_obj = await get_userid_from_username(message.command[1])
                if user_obj == None:
                    return await message.reply_text("I can't find that user")
                user_id = user_obj[0]
                first_name = user_obj[1]

            try:
                reason = message.text.partition(message.command[1])[2]
            except:
                reason = None

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        reason = None
    else:
        await message.reply_text("Please specify a valid user or reply to that user's message")
        return
        
    msg_text, result = await ban_user(client, user_id, first_name, admin_id, admin_name, chat_id, reason)
    if result == True:
        await message.reply_text(msg_text)
    if result == False:
        await message.reply_text(msg_text)


@Client.on_message(filters.command(["unbans"]))
async def unban_command_handler(client, message):
    reason = "okda"
    chat = message.chat
    chat_id = message.chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_restrict_members:
            pass
        else:
            msg_text = "You dont have permission to unban someone"
            return await message.reply_text(msg_text)
    else:
        msg_text = "You dont have permission to unban someone"
        return await message.reply_text(msg_text)

    # Extract the user ID from the command or reply
    if len(message.command) > 1:
        try:
            user_id = int(message.command[1])
            first_name = "User"
        except:
            user_obj = await get_userid_from_username(message.command[1])
            if user_obj == None:
                    return await message.reply_text("I can't find that user")
            user_id = user_obj[0]
            first_name = user_obj[1]

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
    else:
        await message.reply_text("Please specify a valid user or reply to that user's message")
        return
        
    msg_text = await unban_user(client, user_id, first_name, admin_id, admin_name, chat_id)
    await message.reply_text(msg_text)




@Client.on_message(filters.command(["mutes"]))
async def mute_command_handler(client, message):
    reason = "okda"
    chat = message.chat
    chat_id = message.chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_restrict_members:
            pass
        else:
            msg_text = "You dont have permission to mute someone"
            return await message.reply_text(msg_text)
    else:
        msg_text = "You dont have permission to mute someone"
        return await message.reply_text(msg_text)

    # Extract the user ID from the command or reply
    if len(message.command) > 1:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            first_name = message.reply_to_message.from_user.first_name
            reason = message.text.split(None, 1)[1]
        else:
            try:
                user_id = int(message.command[1])
                first_name = "User"
            except:
                user_obj = await get_userid_from_username(message.command[1])
                if user_obj == None:
                    return await message.reply_text("I can't find that user")
                user_id = user_obj[0]
                first_name = user_obj[1]

            try:
                reason = message.text.partition(message.command[1])[2]
            except:
                reason = None

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        reason = None
    else:
        await message.reply_text("Please specify a valid user or reply to that user's message")
        return
    
    msg_text, result = await mute_user(client, user_id, first_name, admin_id, admin_name, chat_id, reason)
    if result == True:
        await message.reply_text(msg_text)
           
    if result == False:
        await message.reply_text(msg_text)


@Client.on_message(filters.command(["unmutes"]))
async def unmute_command_handler(client, message):
    reason = "okda"
    chat = message.chat
    chat_id = message.chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_restrict_members:
            pass
        else:
            msg_text = "You dont have permission to unmute someone"
            return await message.reply_text(msg_text)
    else:
        msg_text = "You dont have permission to unmute someone"
        return await message.reply_text(msg_text)

    # Extract the user ID from the command or reply
    if len(message.command) > 1:
        try:
            user_id = int(message.command[1])
            first_name = "User"
        except:
            user_obj = await get_userid_from_username(message.command[1])
            if user_obj == None:
                    return await message.reply_text("I can't find that user")
            user_id = user_obj[0]
            first_name = user_obj[1]

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
    else:
        await message.reply_text("Please specify a valid user or reply to that user's message")
        return
    chat_id = message.chat.id    
    msg_text = await unmute_user(client, user_id, first_name, admin_id, admin_name, chat_id)
    await message.reply_text(msg_text)





@Client.on_message(filters.command(["tmute"]))
async def tmute_command_handler(client, message):
    reason = "okda"
    chat = message.chat
    chat_id = message.chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_restrict_members:
            pass
        else:
            msg_text = "You dont have permission to mute someone"
            return await message.reply_text(msg_text)
    else:
        msg_text = "You dont have permission to mute someone"
        return await message.reply_text(msg_text)

    # Extract the user ID from the command or reply
    if len(message.command) > 1:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            first_name = message.reply_to_message.from_user.first_name
            time = message.text.split(None, 1)[1]

            try:
                time_amount = time.split(time[-1])[0]
                time_amount = int(time_amount)
            except:
                return await message.reply_text("wrong format!!\nFormat: `/tmute 2m`")

            if time[-1] == "m":
                mute_duration = datetime.timedelta(minutes=time_amount)
            elif time[-1] == "h":
                mute_duration = datetime.timedelta(hours=time_amount)
            elif time[-1] == "d":
                mute_duration = datetime.timedelta(days=time_amount)
            else:
                return await message.reply_text("wrong format!!\nFormat:\nm: Minutes\nh: Hours\nd: Days")
        else:
            try:
                user_id = int(message.command[1])
                first_name = "User"
            except:
                user_obj = await get_userid_from_username(message.command[1])
                if user_obj == None:
                    return await message.reply_text("I can't find that user")
                user_id = user_obj[0]
                first_name = user_obj[1]

            try:
                time = message.text.partition(message.command[1])[2]
                try:
                    time_amount = time.split(time[-1])[0]
                    time_amount = int(time_amount)
                except:
                    return await message.reply_text("wrong format!!\nFormat: `/tmute 2m`")

                if time[-1] == "m":
                    mute_duration = datetime.timedelta(minutes=time_amount)
                elif time[-1] == "h":
                    mute_duration = datetime.timedelta(hours=time_amount)
                elif time[-1] == "d":
                    mute_duration = datetime.timedelta(days=time_amount)
                else:
                    return await message.reply_text("wrong format!!\nFormat:\nm: Minutes\nh: Hours\nd: Days")
            except:
                return await message.reply_text("Please specify a valid user or reply to that user's message\nFormat: `/tmute @user 2m`")

    else:
        await message.reply_text("Please specify a valid user or reply to that user's message\nFormat: /tmute <username> <time>")
        return
    
    msg_text, result = await mute_user(client, user_id, first_name, admin_id, admin_name, chat_id, reason=None, time=mute_duration)
    if result == True:
        await message.reply_text(msg_text)
    if result == False:
        await message.reply_text(msg_text)


@Client.on_message(filters.command("unmuteall") & admin_filter)
async def unmute_all(client, msg):
    chat_id=msg.chat.id   
    user_id=msg.from_user.id
    x = 0
    bot=await client.get_chat_member(chat_id,user_id)
    bot_permission=bot.privileges.can_restrict_members==True 
    if bot_permission:
        banned_users = []
        async for m in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.RESTRICTED):
            banned_users.append(m.user.id)       
            try:
                    await client.restrict_chat_member(chat_id,banned_users[x], ChatPermissions(can_send_messages=True,can_send_media_messages=True,can_send_polls=True,can_add_web_page_previews=True,can_invite_users=True))
                    await msg.reply_text(f"ᴜɴᴍᴜᴛɪɴɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs {m.user.mention}")

                    print(f"ᴜɴᴍᴜᴛɪɴɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs {m.user.mention}")
                    x += 1
                    
                                        
            except Exception as e:
                print(e)
    else:
        await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")
