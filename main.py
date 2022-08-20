"""
Бот для создания профиль-сообщения.
"""
from telebot import TeleBot
from telebot.types import Message
from configs import *
from something import *
import sqlite3

bot = TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['/start', '/delete', '/help', 'myprofiles'])
def starting(message: Message):
    name = message.from_user.full_name
    chat_id = message.chat.id
    photo = open('Desktop/Capture.JPG', 'rb')
    if message.text == '/start':
        bot.send_message(chat_id, f'🙎 Здравствуй <b>{name}</b>, я бот который может создать тебе мини-текстовый профиль.'
                                  f'❔ Незнаешь что такое <b>текстовый профиль</b>? Выбери или нажми на команду <b>/help</b>')
    elif message.text == '/help':
        bot.send_message(chat_id, f'ℹ️<b>Что такое текстовый профиль?</b>'
                                  f'<b>Текстовый профиль</b> - это сообщение или текст, где минимально написана информация о человеке.'
                                  f'<b>ПРИМЕР Текстового профиля:</b>'
                                  f'{photo}')
        bot.send_message(chat_id, f'☑️А теперь когда ты узнал о <b>Текстовых Профилях, почему-бы не создать себе новый профиль?', reply_markup=yesorno())


bot.polling(none_stop=True)
