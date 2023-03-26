from classes import *
from text_data import *

main_menu_text = 'Главное меню'

greetings_message_text = 'Бот HR_SMS&VIV'

modules = [
    Module(Button('ИСТОРИЯ КОМПАНИИ 📖', 'btn1'), history),
    Module(Button('ПОЗДРАВЛЕНИЯ СОТРУДНИКОВ 🎉', 'btn2'), party),
    Module(Button('ПОЛЕЗНЫЕ ССЫЛКИ 🔗', 'btn3'), links),
    Module(Button('НАША МИССИЯ 🎯', 'btn4'), mission),
    Module(Button('В НАШИХ ЦЕННОСТЯХ 📃', 'btn5'), price),
    Module(Button('ПРАВИЛА ПАРКОВКИ 🚘', 'btn6'), parking),
    Module(Button('ДОБРОВОЛЬНОЕ МЕДИЦИНСКОЕ СТРАХОВАНИЕ 🚑', 'btn7'), dms),
    Module(Button('ПРАВИЛА ДРЕСС-КОДА И ОБЩЕНИЯ ВНУТРИ КОМПАНИИ 👔', 'btn8'), dress_code),
    Module(Button('ПРАВИЛА ПОЛЬЗОВАНИЯ ПРОПУСКОМ 🪪', 'btn9'), rules),
    Module(Button('ПРОГРАММЫ ДЛЯ РАБОТЫ 💻', 'btn10'), programs),
]
