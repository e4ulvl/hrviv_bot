import telebot

from config import BOT_API_KEY
from constants import *

from keyboards import reply_keyboard, inline_keyboard_main, inline_keyboard_teleport_1

bot = telebot.TeleBot(BOT_API_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, greetings_message_text, reply_markup=reply_keyboard)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == main_menu_text:
        bot.send_message(message.chat.id, "Наши разделы", reply_markup=inline_keyboard_main)
    elif message.text == teleport_text:
        bot.send_message(message.chat.id, "Телепорт", reply_markup=inline_keyboard_teleport_1)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    ## TODO: переделать на хэш-мап, думаю, будет быстрее, так быдловато
    for m in modules:
        if callback.data == m.button.callback:
            bot.send_message(callback.message.chat.id, m.content, parse_mode='HTML')

bot.polling(none_stop=True)
