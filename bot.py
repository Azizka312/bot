import os
import time
from datetime import datetime
from datetime import date
from dotenv import load_dotenv
import telebot
from telebot import TeleBot
import webbrowser

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['photo'])
def get_reply(message):
    bot.reply_to(message,'ФИГНЯ фото!')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.youtube.com/watch?v=-l_CYgBj4IE&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=2')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,f'SALAM ALEIKUM, {message.from_user.first_name} {message.from_user.username}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,'<b>HELP</b> <em><u>INFO</u></em> ' , parse_mode='HTML')



@bot.message_handler()
def info(message):
    if message.text.lower() == 'Привет':
        bot.send_message(message.chat.id, f'SALAM ALEIKUM, {message.from_user.first_name} {message.from_user.username}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'id: {message.from_user.id}')

bot.infinity_polling()