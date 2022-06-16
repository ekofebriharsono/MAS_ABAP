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

@bot.message_handler(commands=['alvcreate'])
def contactUs(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btnTOP = telebot.types.InlineKeyboardButton("TOP Include", callback_data="top_include_alv")
    markup.add(btnTOP)
    btnGetData = telebot.types.InlineKeyboardButton("Get Data", callback_data="get_data")
    markup.add(btnGetData)
    btnFieldcat = telebot.types.InlineKeyboardButton("Fieldcat", callback_data="fieldcat")
    btnLayout = telebot.types.InlineKeyboardButton("Layout", callback_data="layout")
    markup.add(btnFieldcat, btnLayout)
    btnStatus = telebot.types.InlineKeyboardButton("Status", callback_data="status_alv")
    btnCommand = telebot.types.InlineKeyboardButton("Command", callback_data="command_alv")
    markup.add(btnStatus, btnCommand)
    msg = bot.send_message(message.chat.id, "Create ALV", reply_to_message_id=message.message_id, reply_markup=markup, parse_mode=modeMarkdown)
    bot.register_callback_query_handler(msg, call_handler)

@bot.message_handler(commands=['macroscreate'])
def bapi(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btnMacros1 = telebot.types.InlineKeyboardButton("Sample 1", callback_data="macros_sample_1")
    btnMacros2 = telebot.types.InlineKeyboardButton("Sample 2", callback_data="macros_sample_2")
    markup.add(btnMacros1, btnMacros2)
    msg = bot.send_message(message.chat.id, "Create Macros", reply_to_message_id=message.message_id, reply_markup=markup, parse_mode=modeMarkdown)
    bot.register_callback_query_handler(msg, call_handler)

@bot.message_handler(commands=['contactus'])
def contactUs(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("WhatsApp", url="wa.me/6289607244544")
    button2 = telebot.types.InlineKeyboardButton("Telegram", url='t.me/ekofebriharsono')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, "if there is a problem please contact the developer", reply_to_message_id=message.message_id, reply_markup=markup, parse_mode=modeMarkdown)


@bot.callback_query_handler(func=lambda call:True)
def call_handler(call):
#==============================================================
# Create ALV
#==============================================================
    if call.data == "top_include_alv":
        build_top_alv(call)
    elif call.data == "fieldcat":
        build_fieldcat(call)
    elif call.data == "layout":
        build_layout(call)
    elif call.data == "get_data":
        get_data(call)
#==============================================================
# Create ALV
#==============================================================
#==============================================================
# Create Macros
#==============================================================
    elif call.data == "macros_sample_1":
        sample_macros_1(call)
    elif call.data == "macros_sample_2":
        sample_macros_2(call)
#==============================================================
# Create Macros
#==============================================================


#==============================================================
# Create ALV
#==============================================================
def build_fieldcat(call):
    bot.send_message(call.message.chat.id, t.textCreateALVNote, parse_mode=modeMarkdown)
    bot.send_message(call.message.chat.id, t.textCreateALV, parse_mode=modeMarkdown)

def build_layout(call):
    bot.send_message(call.message.chat.id, t.textCreateLayoutNote, parse_mode=modeMarkdown)
    bot.send_message(call.message.chat.id, t.textCreateLayout, parse_mode=modeMarkdown)

def build_top_alv(call):
    bot.send_message(call.message.chat.id, t.textCreateTOPALV, parse_mode=modeMarkdown)

def get_data(call):
    bot.send_message(call.message.chat.id, t.textCreateGetData, parse_mode=modeMarkdown)
#==============================================================
# Create ALV
#==============================================================

#==============================================================
# Create Macros
#==============================================================
def sample_macros_1(call):
    bot.send_message(call.message.chat.id, t.textCreateMacros1, parse_mode=modeMarkdown)

def sample_macros_2(call):
    bot.send_message(call.message.chat.id, t.textCreateMacros2, parse_mode=modeMarkdown)
#==============================================================
# Create Macros
#==============================================================

while True:
    try:
        bot.polling()
    except:
        pass