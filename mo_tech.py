from pyrogram import Client, filters


Adheera=Client(
    "pyrogrambot",
    bot_token="5523963638:AAECZ3DPolIyPbOSTp1gv5tP6dZjbMXKr-o",
    api_id="10602849",
    api_hash="1d72f2f6623e8f5f31a7db26052791e1"
)

@Adheera.on_message(filters.commamd("start"))  
async def start_message(bot, message):
    await message.reply_text("hi")



Adheera.run()
