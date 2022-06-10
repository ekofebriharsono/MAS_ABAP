# mengimport package pyTelegramBotAPI
import telebot
import text as t

# inisialisasi Token Bot Kita
bot = telebot.TeleBot('5538304225:AAGOS3Fibg_9Ji_seajAfcWPkBzT8Wog6Hw')

# Menghandle Pesan /start
@bot.message_handler(commands=['start'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, t.start)

@bot.message_handler(commands=['abap'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, t.whatIsABAP)

while True:
    try:
        bot.polling()
    except:
        pass