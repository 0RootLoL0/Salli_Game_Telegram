import telebot

bot = telebot.TeleBot("762157084:AAGOAeVgxH7nXxNt-LV4lDZiDOMzux0oS9U")

user_m = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message, "добро пожаловать")
	bot.send_message(message, "Для осмотра состояния нажми 9")
	bot.send_message(message, "для начала отправте любую цыфру")
	user_m[message.chat.id] = {"nickname": message.chat.username, "hard": 10, "hangree": 10,
									  "root_scena": 0, "schena": 0}
	print(user_m)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	print(message.chat.id)
	print(message.text)
	bot.reply_to(message, message.text)

bot.polling()