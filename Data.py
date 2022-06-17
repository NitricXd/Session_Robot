from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🙄 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 🙄", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("❣️ sᴜᴩᴩᴏʀᴛ ❣", url="https://t.me/XCodeSupport")],
        [
            InlineKeyboardButton("🤔 ʜᴏᴡ ᴛᴏ ᴜsᴇ 🤔", callback_data="help"),
            InlineKeyboardButton("🎪 ᴀʙᴏᴜᴛ 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("🥀 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🥀", url="https://t.me/Xd_Nitric")],
    ]

    START = """
Hᴇʏ {},
Tʜɪs ɪs {},
Aɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇᴅ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.
Sᴏᴜʀᴄᴇ : [ɢɪᴛʜᴜʙ](https://github.com/NitricXd/Session_Robot)
Mᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ : [Nitric](https://t.me/Xd_Nitric) !
    """

    HELP = """
✨ **Aᴠᴀɪʟᴀʙʟᴇ Cᴏᴍᴍᴀɴᴅs** ✨

/about - Aʙᴏᴜᴛ Tʜᴇ Bᴏᴛ
/help - Tʜɪs Mᴇssᴀɢᴇ
/start - Sᴛᴀʀᴛ Tʜᴇ Bᴏᴛ
/repo - Gᴇᴛ Rᴇᴘᴏ
/generate - Sᴛᴀʀᴛ Gᴇɴᴇʀᴀᴛɪɴɢ Sᴇssɪᴏɴ
/cancel - Cᴀɴᴄᴇʟ Tʜᴇ Pʀᴏᴄᴇss
/restart - Cᴀɴᴄᴇʟ Tʜᴇ Pʀᴏᴄᴇss
"""

    # About Message
    ABOUT = """
**Aʙᴏᴜᴛ Tʜɪs Bᴏᴛ** 

A ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ & ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ʙʏ @TheXCodeTeam

Source Code : [Click Here](https://t.me/TheXCodeTeam)
Framework : [Pyrogram](docs.pyrogram.org)
Language : [Python](www.python.org)
Developer : @Xd_Nitric
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
💥 A ᴘᴏᴡᴇʀғᴜʟ ʙᴏᴛ
ᴏғ ♻️ Nitric Xd -
━━━━━━━━━━━━━━━━━
GENERATE SESSION FOR TG...
┏━━━━━━━━━━━━━━━━━┓
┣★ [𝐂𝐫𝐞𝐚𝐭𝐨𝐫] [Asad Ali](https://t.me/Xd_Nitric)
┣★ [𝐇𝐞𝐚𝐫𝐭]   [Heart ❤️](https://t.me/XdFamilY)
┣★ [𝐁𝐨𝐭 𝐔𝐩𝐝𝐚𝐭𝐞𝐬] [Our Other Bots](https://t.me/TheXCodeTeam)
┗━━━━━━━━━━━━━━━━━┛
💞 
Iғ Hᴀᴠᴇ Aɴʏ Qᴜᴇsᴛɪᴏɴ Oʀ Wᴀɴᴛ Rᴇᴘᴏ Tʜᴇɴ Cᴏɴᴛᴀᴄᴛ » Tᴏ » Mʏ » [Oᴡɴᴇʀ] @Xd_Nitric.
   """