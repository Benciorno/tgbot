"""
Бот для создания профиль-сообщения.
"""
from telebot import TeleBot
from telebot.types import Message
from configs import *
from something import *
import sqlite3

bot = TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start', 'delete', 'help', 'myprofiles', 'create'])
def starting(message: Message):
    name = message.from_user.full_name
    chat_id = message.chat.id
    example = open("C://Users//ismoi//Desktop//Capture.JPG", 'rb')
    if message.text == '/start':
        bot.send_message(chat_id, f'🙎 Здравствуй <b>{name}</b>, я бот который может создать тебе мини-текстовый профиль.'
                                  f'\n❔ Незнаешь что такое <b>текстовый профиль</b>? Выбери или нажми на команду <b>/help</b>')

    elif message.text == '/help':
        bot.send_message(chat_id, f'ℹ️<b> Что такое текстовый профиль?</b>'
                                  f'\n<b>Текстовый профиль</b> - это сообщение или текст, где минимально написана информация о человеке.'
                                  f'\n<b>ПРИМЕР Текстового профиля:</b>')
        bot.send_photo(chat_id, example)
        bot.send_message(chat_id, "🧐 Если вы поняли что такое <b>Текстовый профиль</b>, то хотите ли вы создать себе новый профиль?", reply_markup=yesorno())

    elif message.text == '/create':
        bot.send_message(chat_id, f'''🧐 Вы хотите начать процесс создания <b>Текстового профиля</b>?''', reply_markup=yesorno())
@bot.message_handler(content_types=['text'])
def startnu2(message: Message):
    chat_id = message.chat.id
    if message.text == 'НЕТ ❌':
        bot.send_message(chat_id, "😉 Мы вас поняли."
                                  "\n♻️ Если вы захотите создать себе <b>Текстовый профиль</b>, то выберите либо нажмите на кнопку <b>/create</b>")
    if message.text == 'ДА ✅':
        bot.send_message(chat_id, f'''❗️Начинаем процесс создания <b>Текстового профиля</b>
<i>❓ Отвечайте на заданные вам вопросы</i>''')

        msg = bot.send_message(chat_id, "❓ <b>Вопрос №1</b>"
                                  "\n🙎 Как вас зовут? <b>(И.Ф.O)</b>")
        bot.register_next_step_handler(msg, phone)
def phone(message: Message):
    chat_id = message.chat.id
    name = message.text
    msg = bot.send_message(chat_id, "❓ <b>Вопрос №2</b>"
                                  "\n☎️ Какой ваш номер телефона?</b>")

    bot.register_next_step_handler(msg, birthdate, name)

def birthdate(message: Message, name):
    chat_id = message.chat.id
    number = message.text
    msg = bot.send_message(chat_id, "❓ <b>Вопрос №3</b>"
                                  "\n📅 Когда вы родились?</b>")

    bot.register_next_step_handler(msg, tag, name, number)

def tag(message: Message, name, number):
    chat_id = message.chat.id
    date = message.text
    msg = bot.send_message(chat_id, "❓ <b>Вопрос №4</b>"
                                  "\n🆔 Какой тег у вашего профиля?</b>")

    bot.register_next_step_handler(msg, descr, name, number, date)

def descr(message: Message, name, number, date):
    chat_id = message.chat.id
    tgtag = message.text
    msg = bot.send_message("❓ <b>Вопрос №4</b>"
                                  "\n🆔 Какое описание будет у вашего профиля?</b>")
    desc = message.text

    database = sqlite3.connect('profiler.db')
    cursor = database.cursor()
    cursor.execute('''
INSERT INTO profile(telegram_id, tag, number, name, birthdate, description)
VALUES (?,?,?,?,?,?)
    ''', (chat_id, tgtag, number, name, date, desc))
    database.commit()
    database.close()




bot.polling(none_stop=True)