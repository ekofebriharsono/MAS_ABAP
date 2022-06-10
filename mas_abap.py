# mengimport package pyTelegramBotAPI
from cgitb import handler, text
import telebot
import text as t

# inisialisasi Token Bot Kita
bot = telebot.TeleBot('5538304225:AAGOS3Fibg_9Ji_seajAfcWPkBzT8Wog6Hw')

modeHTML = 'HTML' 
modeMarkdown = 'Markdown' 

# Menghandle Pesan /start
@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.send_message(message.chat.id, t.start, parse_mode=modeMarkdown)

@bot.message_handler(commands=['abap'])
def abao(message):
    bot.send_message(message.chat.id, t.whatIsABAP, reply_to_message_id=message.message_id, parse_mode=modeMarkdown)

@bot.message_handler(commands=['alv'])
def alv(message):
    bot.send_message(message.chat.id, t.whatIsALV, reply_to_message_id=message.message_id, parse_mode=modeMarkdown)

@bot.message_handler(commands=['bapi'])
def bapi(message):
    bot.send_message(message.chat.id, t.whatIsBAPI, reply_to_message_id=message.message_id, parse_mode=modeMarkdown)

@bot.message_handler(commands=['contactus'])
def contactUs(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("WhatsApp", url="wa.me/6289607244544")
    button2 = telebot.types.InlineKeyboardButton("Telegram", url='t.me/ekofebriharsono')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, "if there is a problem please contact the developer", reply_to_message_id=message.message_id, reply_markup=markup, parse_mode=modeMarkdown)

@bot.message_handler(commands=['alvcreate'])
def contactUs(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("Fieldcat", callback_data="fieldcat")
    button2 = telebot.types.InlineKeyboardButton("Layout", callback_data="layout")
    markup.add(button1, button2)
    msg = bot.send_message(message.chat.id, "Create ALV", reply_to_message_id=message.message_id, reply_markup=markup, parse_mode=modeMarkdown)
    bot.register_callback_query_handler(msg, call_handler_create_alv)

@bot.callback_query_handler(func=lambda call:True)
def call_handler_create_alv(call):
    if call.data == "fieldcat":
        build_fieldcat(call)
    elif call.data == "layout":
        build_layout(call)

def build_fieldcat(call):
    bot.send_message(call.message.chat.id, "Build Fieldcat", parse_mode=modeMarkdown)

def build_layout(call):
    bot.send_message(call.message.chat.id, "Build Layout", parse_mode=modeMarkdown)

while True:
    try:
        bot.polling()
    except:
        pass