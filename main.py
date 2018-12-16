import telebot
import json
from telebot import types

#  ":'######:::::'###::::'##:::::::'##:::::::'####:"
#  ":##... ##:::'## ##::: ##::::::: ##:::::::. ##::"
#  ":##:::..:::'##:. ##:: ##::::::: ##:::::::: ##::"
#  ": ######::'##:::. ##: ##::::::: ##:::::::: ##::"
#  ":..... ##: #########: ##::::::: ##:::::::: ##::"
#  "'##::: ##: ##.... ##: ##::::::: ##:::::::: ##::"
#  ". ######:: ##:::: ##: ########: ########:'####:"
#  ":......:::..:::::..::........::........::....::"
#  telegram bot Game text quest
bot = telebot.TeleBot("733098942:AAESpQhj-4Pt4X3WTSdShUMcFnkTdGRenTE")

json_TextFile = open('continuity.json')
textMess = json.loads(json_TextFile.read())
user_m = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
  photo = open('logotypea.png', 'rb')
  bot.send_photo(message.chat.id, photo)
  bot.send_message(message.chat.id, "добро пожаловать")
  markup = types.ReplyKeyboardMarkup(row_width=1)
  markup.row(types.KeyboardButton("1. открыть дверь"))
  bot.send_message(message.chat.id, textMess[0][0]["text"], reply_markup=markup)
  user_m[message.chat.id] = {"nickname": message.chat.username, "hard": 10, "hangree": 10,"root_scena": 0, "schena": 0, "pred_schena": True}

@bot.message_handler(func=lambda message: True)
def echo_all(message):
  if user_m.get(message.chat.id) != None:
    if user_m[message.chat.id]["pred_schena"]:
      user_m[message.chat.id]["hard"] += textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["Hard"]
      user_m[message.chat.id]["hangree"] += textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["hangre"]

    if str(message.text).split(".")[0] == "1":
      user_m[message.chat.id]["schena"] = textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["otvet"][0]["schena"]
      user_m[message.chat.id]["root_scena"] = textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["root"]
      user_m[message.chat.id]["pred_schena"] = True
    elif str(message.text).split(".")[0] == "2":
      user_m[message.chat.id]["schena"] = textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["otvet"][1]["schena"]
      user_m[message.chat.id]["root_scena"] = textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["root"]
      user_m[message.chat.id]["pred_schena"] = True
    elif str(message.text).split(".")[0] == "9":
      bot.send_message(message.chat.id, "Ед.жизни:  " + str(user_m[message.chat.id]["hard"])+
                       "\nЕд.голода: " + str(user_m[message.chat.id]["hangree"]))
      user_m[message.chat.id]["pred_schena"] = False
    elif str(message.text) == "statistics_0rootlol0":
      bot.send_message(message.chat.id, "количество зарегистрированых Users`:  " + str(len(user_m)))
      user_m[message.chat.id]["pred_schena"] = False
    else:
      bot.send_message(message.chat.id, "error")
      user_m[message.chat.id]["pred_schena"] = False



    markup = types.ReplyKeyboardMarkup(row_width=len(textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["otvet"]))

    for otvet in range(0, len(textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["otvet"])):
        markup.row(types.KeyboardButton(str(otvet + 1) + ". " +textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["otvet"][otvet]["text"]))
    markup.row(types.KeyboardButton("9. моё состояние"))
    bot.send_message(message.chat.id, textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["text"], reply_markup=markup)
  else:
    bot.send_message(message.chat.id, "вы не зарегистриваны для регистрации команда /start")

bot.polling()