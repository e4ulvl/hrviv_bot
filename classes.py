"""Класс объединяющий кнопку и контент, который отправляется по нажатию этой кнопки"""


class Module:
    def __init__(self, button, content):
        self.button = button
        self.content = content


class Button:
    def __init__(self, text, callback):
        self.text = text
        self.callback = callback
