from pyrogram import Client, filters
from pymongo import MongoClient
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid
from pyrogram.types import Message
# -----------------
from info import ADMINS, SUPPORT_CHAT_ID, SUPPORT_CHAT_RULES, MOVIE_RULES, UPDATE_CHANNEL_ID, PRINT_ID, GRP_LNK, LOW_SIZE, SUPPORT_CHAT



# --------------------------------------------------------------------------
mongo_uri = "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority"
database_name = "MONGODB"
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------

mongo_client = MongoClient(mongo_uri)
db = mongo_client[database_name]
top_members_collection = db["rank_db"]

user_data = {}

# ----------------



@Client.on_message(filters.command("rank"))
def top_members(client, message):
    top_members = top_members_collection.find().sort("total_messages", -1).limit(10)
    
    response = "📈 𝖫𝖤𝖠𝖣𝖤𝖱𝖡𝖮𝖠𝖱𝖣\n"
    for idx, member in enumerate(top_members, start=1):
        user_id = member["_id"]
        
        try:
            user = client.get_users(user_id)
            mention = message.from_user.mention if message.from_user else "None"
        except PeerIdInvalid:
            first_name = "Unknown"
        
        total_messages = member["total_messages"]
        user_info = f"{idx}. 👤{message.from_user.mention} •{total_messages}\n"
        response += user_info

    message.reply_text(response)


