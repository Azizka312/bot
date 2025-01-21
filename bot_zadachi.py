import os
import time
from datetime import datetime
from datetime import date
from multiprocessing.resource_tracker import register
from random import random, choice
from dotenv import load_dotenv

load_dotenv()


import telebot
from telebot import types

TOKEN2 = os.getenv("TOKEN2")

Aziz = telebot.TeleBot(token=TOKEN2)
baza_d = []
facts = [
"Медоеды — самые бесстрашные животные на планете.",
    "У осьминогов три сердца и голубая кровь.",
    "Кошки могут поворачивать уши на 180 градусов.",
    "Человеческий мозг имеет примерно 100 миллиардов нейронов.",
    "Пчёлы могут запоминать лица людей.",
    "Язык горилл похож на человеческий, но они не могут говорить.",
    "Слон — единственное животное, которое не может прыгать.",
    "В 2006 году обнаружили новый вид млекопитающих — летающих лемуров.",
    "Медведи — единственные животные, которые могут смотреть на небо, как человек.",
    "Некоторые виды акул могут жить до 400 лет!"
]

@Aziz.message_handler(commands=['start'])
def main(message):
    print("HELLO")
    Aziz.send_message(message.chat.id, f"ПРивет, я ваш помощник! вот что я умею:\n /start \n /help \n /registr \n /fact ")

@Aziz.message_handler(commands=['help'])
def main(message):
    Aziz.send_message(message.chat.id, "ПОМОЩЬ ")

@Aziz.message_handler(commands=['registr'])
def main(message):
    Aziz.send_message(message.chat.id, "Для регистрации напишите свое имя:  ")

@Aziz.message_handler(commands=['fact'])
def main(message):
    Aziz.send_message(message.chat.id, "случайный факт ")


def get_markup():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    item1 =types.KeyboardButton('Регистарция')
    item2 =types.KeyboardButton('Случайный факт')
    item3 =types.KeyboardButton('ПОМОЩЬ!')
    markup.add(item1,item2,item3)
    return markup




@Aziz.message_handler(func=lambda message: message.text == "Регистрация")
def answer_the_message(message):
    Aziz.send_message(message.chat.id, "Напишите свое имя для регистрации: ")

    Aziz.register_next_step_handler(message, register_user)

def register_user(message):
    user_name = message.text.strip()

    if user_name not in baza_d:
        baza_d.append(user_name)
        Aziz.send_message(message.chat.id,f"Регистрация прошла успешно! Привет, {user_name}!")

    else:
        Aziz.send_message(message.chat.id, "ВЫ уже зарегистрированы!")



def fact_world(message):
    random_fact = random.choice(facts)
    Aziz.send_message(message.chat.id,random_fact)

def help_user(message):
    Aziz.send_message(message.chat.id, '/start начать работу с ботом \n'
                                       '/help помощь \n'
                                       '/registr Регистрация \n'
                                       '/fact Случайный факт')






Aziz.infinity_polling()






