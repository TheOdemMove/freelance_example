import telebot
import socket
import os
bot = telebot.TeleBot('610361295:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
sock = socket.socket()

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "test":
        bot.send_message(message.from_user.id, "Тестування: Бот працює стабiльно.")
    elif message.text == "Test":
        bot.send_message(message.from_user.id, "Тестування: Бот працює стабiльно.")
    elif message.text == "TEST":
        bot.send_message(message.from_user.id, "Тестування: Бот працює стабiльно.")
bot.polling(none_stop=True, interval=0)
