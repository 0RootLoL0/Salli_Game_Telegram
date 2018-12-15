import telebot
import re
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

textMess = [[
{
  "text":"Вы видите мрак. Чувствуете холод.  Вы в недоумении. Вдруг ваши веки открылись, и вы встали с холодного пола. Ваша голова раскалывается. На уме только одно. «Где я?».Вы видите небольшую комнату, было темно ,хоть глаз выколи. Вы аккуратно идёте вперёд , и  ощупываете очертания двери.",
  "otvet":[
    {"text":"открыть дверь","schena":1},
  ],
  "Hard":0,
  "hangre":0,
  "root":0
},
{
  "text":"Вы открываете дверь и вдруг вас ослепил свет",
  "otvet":[
    {"text":"вернуться", "schena":2},
    {"text":"двинуться вперёд", "schena":3},
  ],
  "Hard":0,
  "hangre":0,
  "root":0
},
{
   "text":"Вы вернулись в темную комнату",
  "otvet":[
    {"text":"вернуться", "schena":1}
  ],
  "Hard":0,
  "hangre":0,
  "root":0
},
{
  "text":"вы зажмуриваете глаза, и через пару минут вы открываете их. Теперь вы видите гораздо лучше. Это длинный коридор.Вы замечаете: арматуру, и труп",
  "otvet":[
    {"text":"подойти к трупу","schena":4},
    {"text":"взять арматуру","schena":5}
  ],
  "Hard":0,
  "hangre":0,
  "root":0
},
{
  "text":"Вы осматриваете труп и замечаете пулевые отверстия. «что-же здесь было?»",
  "otvet":[
    {"text":"взять арматуру","schena":5}
  ],
  "Hard":0,
  "hangre":0,
  "root":0
},
{
  "text":"Вы берете арматуру «надеюсь она не пригодится» и идете в конец комнаты.Вдруг на вас напала голодная крыса.",
  "otvet":[
    {"text":"ударить","schena":6},
    {"text":"убежать","schena":7}
  ],
  "Hard":0,
  "hangre":0,
  "root":0
},
{
  "text":"Крыса увернулась и укусила вас, но вы все же убиваете её.",
  "otvet":[
    {"text":"...","schena":8}
  ],
  "Hard":0,
  "hangre":0,
  "root":0
},
{
  "text":"вы струсили, и попытались  убежать но крыса успела вас укусить.",
  "otvet":[
    {"text":"...","schena":8}
  ],
  "Hard":0,
  "hangre":0,
  "root":0
},
{
  "text":"Вы осматриваете рану нанесенной ;крысой. Это больно. Но не смертельно -1ед. Жизни. Потом осмотрев коридор чательно, вы видите стол.",
  "otvet":[
    {"text":"Подойти к столу","schena":9}
  ],
  "Hard":-1,
  "hangre":0,
  "root":0
},
{
  "text":"На столе лежит яблоко. Съесть?",
  "otvet":[
    {"text":"да","schena":10},
    {"text":"нет","schena":11}
  ],
  "Hard":0,
  "hangre":0,
  "root":0
},
{
  "text":"+1 ед.Еды",
  "otvet":[
    {"text":"...","schena":12},
  ],
  "Hard":0,
  "hangre":1,
  "root":0
},
{
  "text":"-1 ед.Еды",
  "otvet":[
    {"text":"...","schena":12},
  ],
  "Hard":0,
  "hangre":-1,
  "root":0
},
{
  "text":"Терь вы решаете осмотреть свое состояние и двинуться в путь.",
  "otvet":[
    {"text":"открываете дверь с названием «ВЫХОД»","schena":0}
  ],
  "Hard":0,
  "hangre":0,
  "root":1
}
]]
user_m = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
  photo = open('logotypea.png', 'rb')
  bot.send_photo(message.chat.id, photo)
  bot.send_message(message.chat.id, "добро пожаловать")
  bot.send_message(message.chat.id, textMess[0][0]["text"])
  bot.send_message(message.chat.id, "1. открыть дверь")
  user_m[message.chat.id] = {"nickname": message.chat.username, "hard": 10, "hangree": 10,"root_scena": 0, "schena": 0}

@bot.message_handler(func=lambda message: True)
def echo_all(message):
  if user_m.get(message.chat.id) != None:
    #TODO исправить обработку ошибок бесконечные начисления
    user_m[message.chat.id]["hard"] += textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["Hard"]
    user_m[message.chat.id]["hangree"] += textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["hangre"]

    if str(message.text).split(".")[0] == "1":
      user_m[message.chat.id]["schena"] = textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["otvet"][0]["schena"]
    elif str(message.text).split(".")[0] == "2":
      user_m[message.chat.id]["schena"] = textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["otvet"][1]["schena"]
    elif str(message.text).split(".")[0] == "9":
      bot.send_message(message.chat.id, "Ед.жизни:  " + str(user_m[message.chat.id]["hard"])+
                       "\nЕд.голода: " + str(user_m[message.chat.id]["hangree"]))
    else:
      bot.send_message(message.chat.id, "error")



    markup = types.ReplyKeyboardMarkup(row_width=len(textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["otvet"]))

    for otvet in range(0, len(textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["otvet"])):
        markup.row(types.KeyboardButton(str(otvet + 1) + ". " +textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["otvet"][otvet]["text"]))
    bot.send_message(message.chat.id, textMess[user_m[message.chat.id]["root_scena"]][user_m[message.chat.id]["schena"]]["text"], reply_markup=markup)
  else:
    bot.send_message(message.chat.id, "вы не зарегистриваны для регистрации команда /start")

bot.polling()