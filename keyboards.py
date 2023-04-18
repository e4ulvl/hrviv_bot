from telebot import types
from constants import *

"""Клавиатура в нативной клаве"""
reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
b1 = types.KeyboardButton(text=main_menu_text)
b2 = types.KeyboardButton(text=teleport_text)
reply_keyboard.add(b1, b2)


"""Создание Клавиатуры в чате"""
inline_keyboard_main = types.InlineKeyboardMarkup(row_width=1)
for m in modules:
    inline_keyboard_main.add(types.InlineKeyboardButton(text=m.button.text, callback_data=m.button.callback))

"""Создание клавы для телепорта"""
inline_keyboard_teleport_1 = types.InlineKeyboardMarkup(row_width=1)
for m in modules_1:
    inline_keyboard_teleport_1.add(types.InlineKeyboardButton(text=m.text, url=m.url))
