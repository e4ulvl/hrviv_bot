from telebot import types
from constants import *

"""Клавиатура в нативной клаве"""
reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
b1 = types.KeyboardButton(text=main_menu_text)
reply_keyboard.add(b1)


"""Создание Клавиатуры в чате"""
inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
for m in modules:
    inline_keyboard.add(types.InlineKeyboardButton(text=m.button.text, callback_data=m.button.callback))

