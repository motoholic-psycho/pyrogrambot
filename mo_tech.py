from pyrogram import Client, filters


Adheera=Client(
    "pyrogrambot",
    bot_token="5383228275:AAENO9Z23SL1_mS9KgsyxHDPVxqmyLh9pl0",
    api_id="10602849",
    api_hash="1d72f2f6623e8f5f31a7db26052791e1"
)

@Adheera.on_message(filters.commamd("start"))  
async def start_message(bot, message):
    await message.reply_text("hi")



Adheera.run()
