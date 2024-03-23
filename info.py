import re
from os import getenv
from os import environ
from Script import script 
import os


id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

#LazyRenamer Configs
FLOOD = int(environ.get("FLOOD", "10"))
LAZY_MODE = bool(environ.get("LAZY_MODE", True))
#Add user id of the user in this field those who you want to be Authentic user for file renaming features
lazy_renamers = [int(lazrenamers) if id_pattern.search(lazrenamers) else lazrenamers for lazrenamers in environ.get('LAZY_RENAMERS', '').split()]
LAZY_RENAMERS = (lazy_renamers + ADMINS) if lazy_renamers else []
REQ_CHANNEL = int(environ.get('LOG_CHANNEL'))
DOWNLOAD_LOCATION = "./DOWNLOADS"



# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled((environ.get('USE_CAPTION_FILTER', 'True')), True)

PICS = (environ.get('PICS', 'https://te.legra.ph/file/cce1c345a4a752453a3a3.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://te.legra.ph/file/a27dc8fe434e6b846b0f8.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/6602b32023899c4022323.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://te.legra.ph/file/15c1ad448dfe472a5cbb8.jpg")
SP = (environ.get('SP', 'https://telegra.ph/file/db018384d5d139f3844ed.jpg https://graph.org/file/08716f4c123a758bb570d.jpg https://telegra.ph/file/30c736c93b5ad5c328141.jpg https://graph.org/file/a40b6e72a7ca053948aaa.jpg https://telegra.ph/file/f1565e213ec1a45a27362.jpg https://telegra.ph/file/0c53da8c1598c63e50a6e.jpg https://graph.org/file/931063abebba643e9ce28.jpg https://telegra.ph/file/360d78cf3209429ca8e66.jpg https://graph.org/file/769a3f165ea93706a79cb.jpg https://graph.org/file/78a4dba77c23020729527.jpg')).split()


# Admins, Channels & Users
ADMIN = int(environ.get('ADMINS'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]
SUPPORT_CHAT_ID = [int(chat) if id_pattern.search(chat) else chat for chat in environ.get('SUPPORT_CHAT_ID', '').split()]
LOW_SIZE = environ.get('LOW_SIZE', "")
GRP_LNK = environ.get('GRP_LNK', '')
CHNL_LNK = environ.get('CHNL_LNK', '')
UPDATE_LNK = environ.get('UPDATE_LNK', '')



F_SUB = os.environ.get("FORCE_SUB", "NasraniChatGroup") 
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL_ID')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
# SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = is_enabled((environ.get("NO_RESULTS_MSG", 'False')), False)

# MongoDB information
SECONDDB_URI = environ.get('SECONDDB_URI', None)
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
SECOND_URI = environ.get('DATABASE_URI', "mongodb+srv://Zebhamol:Zebhamol@cluster0.u1mob6u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
SECOND_NAME = environ.get('DATABASE_NAME', "Cluster0")

COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
GROUP_LOGS = int(environ.get('GROUP_LOGS', 0)) # Request Verification => S - 3
VERIFY = bool(environ.get('VERIFY',False))
IS_VERIFY = is_enabled((environ.get('IS_VERIFY', 'False')), False)
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', "https://t.me/c/1845700490/3")
VERIFY2_URL = environ.get('VERIFY2_URL', "mdisklink.link")
VERIFY2_API = environ.get('VERIFY2_API', "4fa150d44b4bf6579c24b33bbbb786dbfb4fc673")
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'clicksfly.com')
SHORTLINK_API = environ.get('SHORTLINK_API', 'c2150e28189cefefd05f8a9c5c5770cc462033e3')
IS_SHORTLINK = is_enabled((environ.get('IS_SHORTLINK', 'False')), False)
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ ?')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'NASRANI_SUPPORT')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CUSTOM_FILE_CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

TUTORIAL = environ.get('TUTORIAL', 'https://t.me/+r_y-yTPhXkQwMzdl')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))

 
CUSTOM_QUERY_CAPTION = environ.get("CUSTOM_QUERY_CAPTION", f"{script.CUSTOM_QUERY_CAPTION}")
# VERIFY = bool(environ.get('VERIFY', False))
# UPLOAD_CHANNEL = environ.get('UPLOAD_CHANNEL',"https://t.me/batchfiles_store")
#redict
MAIN_CHANNEL = environ.get('MAIN_CHANNEL',"https://t.me/nasrani_update")
FILE_FORWARD = environ.get('FILE_FORWARD',"https://t.me/+7oxSIxY4X0c2ZGVl")
MSG_ALRT = environ.get('MSG_ALRT', '𝑪𝑯𝑬𝑪𝑲 & 𝑻𝑹𝒀 𝑨𝑳𝑳 𝑴𝒀 𝑭𝑬𝑨𝑻𝑼𝑹𝑬𝑺')
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', "-1001708959708"))

BR_IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.BR_TEMPLATE_TXT}")
BATCH_LINK = environ.get('BATCH_LINK',"https://t.me/nasrani_update")
PRINT = environ.get('PRINT',"https://t.me/+IpB01WFvsNplZDI9")
ACCOUNT = environ.get('ACCOUNT', "")



LOW_SIZE = environ.get('LOW_SIZE',"NASRANI_SUPPORT")
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'NASRANI_SUPPORT')
SUPPORT_CHAT_LINK = environ.get('SUPPORT_CHAT_LINK', 't.me/NASRANI_SUPPORT')
UPDATE_CHANNEL_ID = int(environ.get('UPDATE_CHANNEL_ID', 0))
PRINT_ID = int(environ.get('PRINT_ID', 0))
MOVIE_RULES = environ.get('MOVIE_RULES', 't.me/NASRANI_SUPPORT')
SUPPORT_CHAT_RULES = environ.get('SUPPORT_CHAT_RULES', 't.me/NASRANI_SUPPORT')




# LANGUAGES1 = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]
LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan", "s01" , "s02" , "s03" , "s04", "s05" , "s06" , "s07" , "s08" , "s09" , "s10", "144p", "240p", "360p", "480p", "720p", "1080p", "2060p"]


# heroku
HRK_APP_NAME = environ.get('HRK_APP_NAME', 'mybots')
HRK_API = environ.get('HRK_API', '0')
OWNER_USERNAME = getenv("OWNER_USERNAME","Rax_xt")

#### KANG STCKER ####
# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "")
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME" , "JAAMBOOBOT")



LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
