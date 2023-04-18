from classes import *
from text_data import *

main_menu_text = 'Главное меню'
teleport_text = 'Телепорт'

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

modules_1 = [
    LinkModule('Основной ежегодный оплачиваемый отпуск', 'https://docs.google.com/document/d/1Bua3zcyyoJ6X7JjUXnUThm3y7zGh4GotTSRzDDxhyvs/edit'),
    LinkModule('Неоплачиваемый отпуск', 'https://docs.google.com/document/d/1N6aZmJsNwQIPc6Izxasb11IfXyetrkcuplAO9S4hmag/edit'),
    LinkModule('Заявление на учебный отпуск', 'https://docs.google.com/document/d/1cq1A4XQmJHeNmpRfVWN26OLZ4GyROITOlvT2-8g6At4/edit#'),
]
