import webbrowser
from gc import callbacks


import telebot
from telebot import types


bot = telebot.TeleBot(token="7894859862:AAFh5_-VAu1TfCy5-OL4ZsMNjyJlLq3FN8c")

@bot.message_handler(content_types=['photo'])
def photo(message):
    kb= types.InlineKeyboardMarkup()
    btn= types.InlineKeyboardButton(text='Go to site', url='https://beautifulfonts.net/' )
    kb.add(btn)




@bot.message_handler(commands=["start"])
def start(message):
    name = message.from_user.first_name
    bot.send_message(message.from_user.id, f"Hello, {name}")
    bot.register_next_step_handler(message, name, number)
def number(message, name):
    bot.send_message(message.from_user.id, f"Hello, {name} please send your phone number!")

@bot.message_handler(commands=["help"])
def help_user(message):
    bot.send_message(message.from_user.id , "This bot can do anything")

@bot.message_handler()

def info(message):
    if message.text.lower() == "my id":
        user_id = message.from_user.id
        bot.send_message( user_id, f" Your id:{user_id}")
    elif message.text.lower() == "hello":
        user_id = message.from_user.id
        bot.send_message(user_id, f"Hello, {message.from_user.first_name}")
    elif message.text.lower() == "chatgpt":
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Go to the site" , url='https://chatgpt.com/'))
        bot.send_message( user_id ,"The ChatGpt" , reply_markup=markup)
    elif message.text.lower() == "moon":
        user_id = message.from_user.id
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Moonlight", url='https://yandex.ru/images/search?text=moonlight+&pos=2&rpt=simage&img_url=https%3A%2F%2Fimg.goodfon.ru%2Foriginal%2F7288x4864%2Fa%2F81%2Fluna-reka-riab-na-vode-odinokoe-derevo-noch.jpg&from=tabbar&lr=10335'))
        bot.send_message(user_id, "The Moon", reply_markup=markup)

@bot.message_handler(commands=["website"])
def site(message):
    webbrowser.open('https://beautifulfonts.net/')


bot.infinity_polling()


