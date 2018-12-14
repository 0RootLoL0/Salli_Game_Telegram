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
	# '''
	if message.text != "/start":
		bot.send_message(
			textMess[user_m[update.message.chat.id]["root_scena"]][user_m[update.message.chat.id]["schena"]][
				"text"])
		# hard & hangree
		user_m[update.message.chat.id]["hard"] += \
			textMess[user_m[update.message.chat.id]["root_scena"]][user_m[update.message.chat.id]["schena"]][
				"Hard"]
		user_m[update.message.chat.id]["hangree"] += \
			textMess[user_m[update.message.chat.id]["root_scena"]][user_m[update.message.chat.id]["schena"]][
				"hangre"]

		for otvet in range(0, len(textMess[user_m[update.message.chat.id]["root_scena"]][
									  user_m[update.message.chat.id]["schena"]]["otvet"])):
			update.message.reply_text(str(otvet + 1) + ". " +
									  textMess[user_m[update.message.chat.id]["root_scena"]][
										  user_m[update.message.chat.id]["schena"]]["otvet"][otvet]["text"])
		print("кто: " + update.message.chat.username)
		print("text: " + update.message.text)
		if str(update.message.text) == '1':
			user_m[update.message.chat.id]["schena"] = \
				textMess[user_m[update.message.chat.id]["root_scena"]][
					user_m[update.message.chat.id]["schena"]][
					"otvet"][0]["schena"]
		elif str(update.message.text) == '2':
			user_m[update.message.chat.id]["schena"] = \
				textMess[user_m[update.message.chat.id]["root_scena"]][
					user_m[update.message.chat.id]["schena"]][
					"otvet"][1]["schena"]
		elif str(update.message.text) == '9':
			message.send_message("Ед.жизни:  " + str(user_m[update.message.chat.id]["hard"]))
			message.send_message("Ед.голода: " + str(user_m[update.message.chat.id]["hangree"]))
		else:
			update.message.reply_text("вы ошиблись")
	else:
		update.message.reply_text("добро пожаловать")
		update.message.reply_text("Для осмотра состояния нажми 9")
		update.message.reply_text("для начала отправте любую цыфру")
		user_m[update.message.chat.id] = {"nickname": update.message.chat.username, "hard": 10, "hangree": 10,
										  "root_scena": 0, "schena": 0}
		print(user_m)
	bot.reply_to(message, message.text)

bot.polling()