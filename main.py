import telebot

bot = telebot.TeleBot("762157084:AAGOAeVgxH7nXxNt-LV4lDZiDOMzux0oS9U")

user_m = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "добро пожаловать")
	bot.send_message(message.chat.id, "Для осмотра состояния нажми 9")
	bot.send_message(message.chat.id, "для начала отправте любую цыфру")
	user_m[message.chat.id] = {"nickname": message.chat.username, "hard": 10, "hangree": 10,"root_scena": 0, "schena": 0}

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if user_m.get(message.chat.id) != None:
        bot.send_message(message.chat.id, message.text)
    else:
        bot.send_message(message.chat.id, "вы не зарегистриваны")

bot.polling()