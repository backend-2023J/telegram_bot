from telegram import Bot
import os 

TOKEN = os.environ['TOKEN']

# Create a bot object
bot = Bot(TOKEN)

update = bot.getUpdates()

chat_id = update.message.chat.id
text = update.message.text
# Print the bot info

phone = "+998931234567"
first_name = "Bilol"
# last_name = "Husanov"

msg = bot.sendContact(chat_id=chat_id, phone_number=phone, first_name=first_name, last_name=None)
print(msg)