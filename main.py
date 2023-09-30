from telegram import Bot
# import os 

# Get the token from the environment variables
TOKEN = '6388893107:AAHm55DuPheZmctXz5mX5HnSfD9zfgmpNhY'
# Create a bot object
bot = Bot(TOKEN)

update = bot.getUpdates()

chat_id = update.message.chat.id
text = update.message.text
# Print the bot info


msg = bot.sendMessage(chat_id, text)
print(msg.text)