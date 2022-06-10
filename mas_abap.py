# mengimport package pyTelegramBotAPI
import telebot
import text as t

# inisialisasi Token Bot Kita
bot = telebot.TeleBot('5538304225:AAGOS3Fibg_9Ji_seajAfcWPkBzT8Wog6Hw')

modeHTML = 'HTML' 
modeMarkdown = 'Markdown' 

# Menghandle Pesan /start
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, t.start, parse_mode=modeMarkdown)

@bot.message_handler(commands=['abap'])
def welcome(message):
    bot.send_message(message.chat.id, t.whatIsABAP, reply_to_message_id=message.message_id, parse_mode=modeMarkdown)

@bot.message_handler(commands=['alv'])
def welcome(message):
    bot.send_message(message.chat.id, t.whatIsALV, reply_to_message_id=message.message_id, parse_mode=modeMarkdown)

@bot.message_handler(commands=['bapi'])
def welcome(message):
    bot.send_message(message.chat.id, t.whatIsBAPI, reply_to_message_id=message.message_id, parse_mode=modeMarkdown)

while True:
    try:
        bot.polling()
    except:
        pass