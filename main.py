import telebot
import json
from telebot import types

with open('continuity.json') as f:
  textMess = json.load(f)

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
with open('user.json') as fa:
  user_m = json.load(fa)

@bot.message_handler(commands=['statistics_0rootlol0'])
def statistics_0rootlol0(message):
  bot.send_message(message.chat.id, "количество зарегистрированых Users`:  " + str(len(user_m)))
  user_m[message.chat.id]["pred_schena"] = False

def condition(message):
  bot.send_message(message.chat.id, "Ед.жизни:  " + str(user_m[message.chat.id]["hard"]) +
                                  "\nЕд.голода: " + str(user_m[message.chat.id]["hangree"]))
  user_m[message.chat.id]["pred_schena"] = False

def teleport(message, numOtvet):
  user_m[message.chat.id]["schena"] = textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["otvet"][numOtvet]["schena"]
  user_m[message.chat.id]["root_scena"] = textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["root"]
  user_m[message.chat.id]["pred_schena"] = True

def teleport_admin(message):
  if int(str(message.text).split("_")[1]) <= len(textMess)-1 and int(str(message.text).split("_")[2]) >= 0 and int(str(message.text).split("_")[1]) <= len(textMess[int(str(message.text).split("_")[1])])-1:
    user_m[message.chat.id]["root_scena"] = int(str(message.text).split("_")[1])
    user_m[message.chat.id]["schena"] = int(str(message.text).split("_")[2])
    user_m[message.chat.id]["pred_schena"] = False

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
      teleport(message, 0)
    elif str(message.text).split(".")[0] == "2" and  len(textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["otvet"]) >= 2:
      teleport(message, 1)
    elif str(message.text).split(".")[0] == "3" and  len(textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["otvet"]) >= 3:
      teleport(message, 2)
    elif str(message.text).split(".")[0] == "4" and  len(textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["otvet"]) >= 4:
      teleport(message, 3)
    elif str(message.text).split(".")[0] == "5" and  len(textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["otvet"]) >= 5:
      teleport(message, 4)
    elif str(message.text).split(".")[0] == "9":
      condition(message)
    elif str(message.text).split("_")[0] == "/teleportAadmin":
      teleport_admin(message)
    else:
      bot.send_message(message.chat.id, "error")
      user_m[message.chat.id]["pred_schena"] = False

    with open('user1.json', 'w') as outfile:
      json.dump(user_m, outfile)

    markup = types.ReplyKeyboardMarkup(row_width=len(textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["otvet"]))

    for otvet in range(0, len(textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["otvet"])):
        markup.row(types.KeyboardButton(str(otvet + 1) + ". " +textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["otvet"][otvet]["text"]))
    markup.row(types.KeyboardButton("9. моё состояние"))
    bot.send_message(message.chat.id, textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["text"], reply_markup=markup)
  else:
    bot.send_message(message.chat.id, "вы не зарегистриваны для регистрации команда /start")

bot.polling()