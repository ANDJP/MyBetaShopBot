import telebot
from telebot import types
import random

bot = telebot.TeleBot('YourToken')

@bot.message_handler(commands=['start'])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Наши соц-сети 👥')
    btn2 = types.KeyboardButton('Получить чек 🧾')
    btn3 = types.KeyboardButton('Заказать 🛒')

    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, 'Привет я beta версия магазина. \nКсати неплохое имя {0.first_name} '.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def button(message):
    if message.text == 'Наши соц-сети 👥':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Инстаграм 📷')
        item2 = types.KeyboardButton('Ютуб канал 📺')
        item3 = types.KeyboardButton('Наш теллеграм канал 👀')
        item4 = types.KeyboardButton('⬅️ Вернуться назад')

        markup.add(item1, item2, item3, item4)

        bot.send_message(message.chat.id, 'Наши соц-сети 👥', reply_markup=markup)

    elif message.text == 'Получить чек 🧾':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton('Чек о покупке 📝')
        item2 = types.KeyboardButton('Поддержка ❤️‍🩹')
        item3 = types.KeyboardButton('⬅️ Вернуться назад')

        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id, 'Получить чек 🧾', reply_markup=markup)


    elif message.text == 'Заказать 🛒':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Тетради 📕')
        item2 = types.KeyboardButton('Кружки 🥤️')
        item3 = types.KeyboardButton('Одежда 👕')
        item4 = types.KeyboardButton('⬅️ Вернуться назад')

        markup.add(item1, item2, item3, item4)

        bot.send_message(message.chat.id, 'Товары:', reply_markup=markup)

    elif message.text == 'Инстаграм 📷':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Перейти в Instagram', url='https://www.instagram.com/remyghaa'))
        bot.send_message(message.chat.id, 'Наш instagram аккаунт ⬇️', reply_markup=markup)

    elif message.text == 'Ютуб канал 📺':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Перейти на YouTube', url='https://www.youtube.com/c/andrushahope'))
        bot.send_message(message.chat.id, 'Наш YouTube канал ⬇️', reply_markup=markup)


    elif message.text == 'Наш теллеграм канал 👀':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Перейти на Telegram канал', url='https://t.me/AndrushaHopeYT'))
        bot.send_message(message.chat.id, 'Наш теллеграм канал ⬇️', reply_markup=markup)

    elif message.text == '⬅️ Вернуться назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Наши соц-сети 👥')
        btn2 = types.KeyboardButton('Получить чек 🧾')
        btn3 = types.KeyboardButton('Заказать 🛒')

        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id, 'Вы вернулись назад', reply_markup=markup)

    elif message.text == 'Чек о покупке 📝':
        bot.send_message(message.chat.id, 'Ваш номер чека: ' + str(random.randint(100, 10000)))

    # elif message.text == 'Одежда 👕':
    #     photo = open('кепка.jpg', 'rb')
    #     markup = types.InlineKeyboardMarkup()
    #     markup.add(types.InlineKeyboardMarkup, photo)
    #     bot.send_photo(message.chat.id, 'Заказать', reply_markup=markup)

bot.polling(none_stop=True)