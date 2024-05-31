import telebot
from telebot import types

bot = telebot.TeleBot("6306663999:AAGjz35dixzp--6BOFSAxKqoCMkjsYHs5d4")

recommendations = [
    "Инвентаризация чувствительных данных. Рассмотрим какие существуют важные данные и как следует их защитить?",
    "Сегодня необходимо придумать новый пароль для аккаунтов в социальных сетях.",
    "Защита почтовых ящиков. Зайдите в свой почтовый ящик, далее «Настройки», далее «Безопасность», далее «Сменить пароль»."
   
]


def display_recommendations(user_id, page):
    start_index = (page - 1) * 5
    end_index = min(start_index + 5, len(recommendations))
    for i in range(start_index, end_index):
        recommendation = recommendations[i]
       
        if is_completed(user_id, i + 1):
            bot.send_message(user_id, f"✅ День {i + 1}. {recommendation}", parse_mode="Markdown")
        elif is_postponed(user_id, i + 1):
            bot.send_message(user_id, f"🔴 День {i + 1}. {recommendation}", parse_mode="Markdown")
        else:
            bot.send_message(user_id, f"⚫️ День {i + 1}. {recommendation}", parse_mode="Markdown")


def is_completed(user_id, recommendation_number):
    pass

def is_postponed(user_id, recommendation_number):
    pass

@bot.message_handler(func=lambda message: True, content_types=['text'])
def view_recommendations(message):
    if message.text == "Рекомендации":
        display_recommendations(message.chat.id, 1)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add(types.KeyboardButton("Показать далее…"))
        markup.add(types.KeyboardButton("Изменить статус выполнения"))
        markup.add(types.KeyboardButton("Меню"))
        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def change_recommendation_status(message):
    if message.text == "Изменить статус выполнения":
        bot.reply_to(message, "Укажите номер рекомендации, статус которого вы хотите изменить и отправьте боту.")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def invite_friends(message):
    if message.text == "Пригласить друзей":
        pass

@bot.message_handler(func=lambda message: True, content_types=['text'])
def take_cyber_hygiene_test(message):
    if message.text == "Пройти тест по цифровой гигиене":
        pass

bot.polling()
