import telepot
token = 'token'
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe())
print ("\n")
print (TelegramBot.getUpdates())

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    name = msg["from"]["first_name"]
    if content_type == 'text':
        bot.sendMessage(chat_id, 'ciao ' + name)

bot = telepot.Bot(token)
bot.message_loop(on_chat_message)

print ("Listening ...")

import time
while 1:
    time.sleep(10)
