from telebot import types
from telebot.types import InlineKeyboardButton


def main_menu():
    kb = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton("sum")
    button2 = types.KeyboardButton("dollar")
    button3= types.KeyboardButton("euro")
    kb.add(button1 , button2 , button3)


