import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'TgMovieSearchRequestBot')
API_ID = int(environ.get('API_ID', '19491592'))
API_HASH = environ.get('API_HASH', '01a4118f7aec3b2caece77a057fdd197')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

#Port
PORT = environ.get("PORT", "8080")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://te.legra.ph/file/3a8d252ba431d035a2224.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001589316857 -1001869924693 -1001446583785 -1001807477865 -1001747347582 -1001647655116').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001758096945')
auth_grp = environ.get('AUTH_GROUP', '-1001804839194')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Telegram")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001875704370'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'USE_FULL_BOTZ_SUPPORT')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "{file_caption}\n\n<b>⍟──❰ 💝 [𝚄𝚂𝙴 𝙵𝚄𝙻𝙻 𝙱𝙾𝚃𝚉](https://telegram.me/use_full_botz) 💝 ❱──⍟\n\n𝚃𝚑𝚒𝚜 𝙵𝚒𝚕𝚎 𝚆𝚒𝚕𝚕 𝙱𝚎 𝙳𝚎𝚕𝚎𝚝𝚎𝚍 𝚆𝚒𝚝𝚑𝚒𝚗 5 𝙼𝚒𝚗𝚞𝚝𝚎𝚜, 𝚂𝚘 𝙵𝚘𝚛𝚠𝚊𝚛𝚍 𝙸𝚝 𝚃𝚘 𝚈𝚘𝚞𝚛 𝚂𝚊𝚟𝚎𝚍 𝙼𝚎𝚜𝚜𝚊𝚐𝚎𝚜, 𝚃𝚑𝚎𝚗 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝙸𝚝 𝙵𝚛𝚘𝚖 𝚂𝚊𝚟𝚎𝚍 𝙼𝚎𝚜𝚜𝚊𝚐𝚎𝚜.\n\n⍟──❰ 💝 [𝚄𝚂𝙴 𝙵𝚄𝙻𝙻 𝙱𝙾𝚃𝚉](https://telegram.me/use_full_botz) 💝 ❱──⍟</b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "{file_caption}\n\n<b>⍟──❰ 💝 [𝚄𝚂𝙴 𝙵𝚄𝙻𝙻 𝙱𝙾𝚃𝚉](https://telegram.me/use_full_botz) 💝 ❱──⍟\n\n𝚃𝚑𝚒𝚜 𝙵𝚒𝚕𝚎 𝚆𝚒𝚕𝚕 𝙱𝚎 𝙳𝚎𝚕𝚎𝚝𝚎𝚍 𝚆𝚒𝚝𝚑𝚒𝚗 5 𝙼𝚒𝚗𝚞𝚝𝚎𝚜, 𝚂𝚘 𝙵𝚘𝚛𝚠𝚊𝚛𝚍 𝙸𝚝 𝚃𝚘 𝚈𝚘𝚞𝚛 𝚂𝚊𝚟𝚎𝚍 𝙼𝚎𝚜𝚜𝚊𝚐𝚎𝚜, 𝚃𝚑𝚎𝚗 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝙸𝚝 𝙵𝚛𝚘𝚖 𝚂𝚊𝚟𝚎𝚍 𝙼𝚎𝚜𝚜𝚊𝚐𝚎𝚜.\n\n⍟──❰ 💝 [𝚄𝚂𝙴 𝙵𝚄𝙻𝙻 𝙱𝙾𝚃𝚉](https://telegram.me/use_full_botz) 💝 ❱──⍟</b>")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🧿 ᴛɪᴛᴛʟᴇ :  {title} \n🌟 ʀᴀᴛɪɴɢ : {rating} \n🎭 ɢᴇɴʀᴇ : {genres} \n📆 ʀᴇʟᴇᴀsᴇ : {year} \n⏰ ᴅᴜʀᴀᴛɪᴏɴ : {runtime} \n🎙️ʟᴀɴɢᴜᴀɢᴇ : {languages} \n🔖 sʜᴏʀᴛ : {plot} \n★ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @USE_FULL_BOTZ")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001589316857 -1001869924693 -1001446583785 -1001807477865 -1001747347582 -1001647655116')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), True)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

## EXTRA FEATURES ##
    
      # URL Shortener #

URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'OmegaLinks.in')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '291045271e395bb939a30ef297067201ab32fb10')

     # Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 600))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

    # Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://telegram.me/How_To_Download_1/"

   # Custom Caption Under Button #
CAPTION_BUTTON = "❤️‍🔥 Join & Support ❤️‍🔥"
CAPTION_BUTTON_URL = "https://telegram.me/USE_FULL_BOTZ"

   # Auto Delete For Bot Sending Files #
