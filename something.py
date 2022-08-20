from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from configs import YN


def yesorno():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = []

    for button in YN.values():
        btn = KeyboardButton(text=button)
        buttons.append(btn)
    markup.add(*buttons)
    return markup