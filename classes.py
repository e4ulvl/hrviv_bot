"""Класс объединяющий кнопку и контент, который отправляется по нажатию этой кнопки"""

"""Модуль для кнопок с текстовым контентом, который отправляется в сообщении"""
class Module:
    def __init__(self, button, content):
        self.button = button
        self.content = content

"""Модуль для кнопок со ссылками"""
class LinkModule:
    def __init__(self, text, url):
        self.text = text
        self.url = url

class Button:
    def __init__(self, text, callback):
        self.text = text
        self.callback = callback
