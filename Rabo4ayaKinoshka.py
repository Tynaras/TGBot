import telebot;
from telebot import apihelper


bot = telebot.TeleBot('1015825681:AAHVc6PtaQNG4E2kY574TgRY0yYunmqjPbk');
# Подключаем модуль случайных чисел 
import random

 
# Подключаем модуль для Телеграма

import telebot

# Указываем токен

bot = telebot.TeleBot('1015825681:AAHVc6PtaQNG4E2kY574TgRY0yYunmqjPbk')

 
# Импортируем типы из модуля, чтобы создавать кнопки

from telebot import types

 
# Заготовки для жанров

comedy = ["Я худею"] or ["Али рули"] or ["Зачинщики"] 

 
uzhasi = ["Чужой","Чужие","Сонная лощина","Пила 3"]
 
boevic = ["Леон","Большой куш","Брат","Апокалипсис"]

 
luchaya = ["Форест Гамп","Зеленая миля","Начало","1+1"]

drama = ["Гладиатор","Достутачаться до небес","Престиж","1+1"] 

mult = ["Валл-и","Балто","Как приручить дракона","9"]

fantastic = ["Интерстеллар","Темный рыцарь"] 

triller = ["Адвокат дьявола","Джокер"]

# Метод, который получает сообщения и обрабатывает их

@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    # Если написали «Подскажи фильм»

    if message.text == "Подскажи фильм":

        # Пишем приветствие

        bot.send_message(message.from_user.id, "Привет, выбери жанр и я подскажу тебе хороший фильм :) .")

        # Готовим кнопки

        keyboard = types.InlineKeyboardMarkup()

        # По очереди готовим текст и обработчик для каждого жанра фильма

        key_comedy = types.InlineKeyboardButton(text='Комедия', callback_data='comedy')

        # И добавляем кнопку на экран

        keyboard.add(key_comedy)

        key_uzhasi = types.InlineKeyboardButton(text='Ужасы', callback_data='uzhasi')

        keyboard.add(key_uzhasi)

        key_boevic = types.InlineKeyboardButton(text='Боевик', callback_data='boevic')

        keyboard.add(key_boevic)

        key_luchaya = types.InlineKeyboardButton(text='Лучшая коллекция фильмов', callback_data='luchaya')

        keyboard.add(key_luchaya)

        key_drama = types.InlineKeyboardButton(text='Драма', callback_data='drama')

        keyboard.add(key_drama)

        key_mult = types.InlineKeyboardButton(text='Мультфильм', callback_data='mult')

        keyboard.add(key_mult)

        key_fantastic = types.InlineKeyboardButton(text='Фантастика', callback_data='fantastic')

        keyboard.add(key_fantastic)

        key_triller = types.InlineKeyboardButton(text='Триллер', callback_data='triller')

        keyboard.add(key_triller)


        # Показываем все кнопки сразу и пишем сообщение о выборе

        bot.send_message(message.from_user.id, text='Выбери жанр', reply_markup=keyboard)

    elif message.text == "/help":

        bot.send_message(message.from_user.id, "'Напиши Подскажи фильм'")

    else:

        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

 
# Обработчик нажатий на кнопки

@bot.callback_query_handler(func=lambda call: True)

def callback_worker(call):

    # Если нажали на одну из 12 кнопок — выводим фильм

    if call.data == "comedy": 
        msg = random.choice(comedy) + ' '
    if call.data == "uzhasi":
        msg = random.choice(uzhasi) + ' '
    if call.data == "boevic":
        msg = random.choice(boevic) + ' '
    if call.data == "luchaya":
         msg = random.choice(luchaya) + ' '
    if call.data == "drama":
        msg = random.choice(drama) + ' '
    if call.data == "mult":
        msg = random.choice(mult) + ' '
    if call.data == "triller":
        msg = random.choice(triller) + ' '
    if call.data == "fantastic":
        msg = random.choice(fantastic) + ' '
    






    # Отправляем текст в Телеграм

    bot.send_message(call.message.chat.id, msg)
 
# Запускаем постоянный опрос бота в Телеграме

bot.polling(none_stop=True, interval=0)