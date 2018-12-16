import telebot
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

# TODO вынести всё в отдельный файл
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
],[
{
  "text":"что-же здесь произошло» открыв дверь вы увидели небольшую комнату. На стенах были засохшие брызги крови, на полу валялись гильзы.\nОсмотрев комнату вы находите: план эвакуации, лифт, и две двери. На одной написано «ВЫХОД»",
  "otvet":[
    {"text":"Осмотреть гильзы","schena":1},
    {"text":"Осмотреть план эвакуации","schena":2},
    {"text":"Вызвать лифт","schena":3},
    {"text":"Открыть дверь с надписью выход","schena":4},
    {"text":"Открыть вторую дверь","schena":5}
  ],
  "Hard":0,
  "hangre":0,
  "root":1
},
{
  "text":"Вы осматриваете гильзы, похоже они свежие.",
  "otvet":[
    {"text":"Вернуться","schena":0}
  ],
  "Hard":0,
  "hangre":0,
  "root":1
},
{
  "text":"«планировка эвакуации сектора А12»",
  "otvet":[
    {"text":"Вернуться","schena":0}
  ],
  "Hard":0,
  "hangre":0,
  "root":1
},

{
  "text":"Вы вызываете лифт… он открывается. Раздался электронный голос «минус четвертый этаж»",
  "otvet":[
    {"text":"Вернуться","schena":8},
    {"text":"Зайти в лифт","schena":9}
  ],
  "Hard":0,
  "hangre":0,
  "root":1
},
{
  "text":"вы видите лестницу, она идёт вниз и вверх",
  "otvet":[
    {"text":"вверх","schena":6},
    {"text":"вниз","schena":7}
  ],
  "Hard":0,
  "hangre":0,
  "root":1
},
{
  "text":"вы открываете дверь, и видите страшную металлическую статую. Вдруг она включается и говорит: «режим сканирования. Цель обнаружена» не успев и глазом моргнуть как вас расстреливает дроид. Вы падаете на пол, истекая кровью. Все окружение стало темнеть. И темнеть. И темнеть…. Вы погибли. Теперь вы можете начать с самого начала, или приложить игру через 1 мин.",
  "otvet":[
  ],
  "Hard":-10,
  "hangre":-10,
  "root":1
},

{
  "text":"вы поднимаетесь на верх. Вот и выход. Вы подходите к большим металлическим воротам. Они закрыты Вряд ли вам удастся их открыть. Вы видите труп. Осмотрев его, вы нашли сумку.\nв сумме вы нашли бинты. +2 ед жизни. --- 20%",
  "otvet":[
    {"text":"вернуться","schena":3}
  ],
  "Hard":2,
  "hangre":0,
  "root":1
},
{
  "text":"вы решили спуститься в самый низ. Вам страшно. Но вас зовет  неизвестность.\n(конец. скоро будет продолжение)",
  "otvet":[
  ],
  "Hard":0,
  "hangre":0,
  "root":1
},
{
  "text":"Хех нет ничего это затычка",
  "otvet":[
    {"text":"в начало Root 1","schena":0}
  ],
  "Hard":0,
  "hangre":0,
  "root":1
},

{
  "text":"вы заходите в лифт, он ещё  работает. Можно спуститься вниз и на верх",
  "otvet":[
    {"text":"наверх","schena":10},
    {"text":"вниз","schena":11}
  ],
  "Hard":0,
  "hangre":0,
  "root":1
},
{
  "text":"нажимаете на кнопку -1. Лифт начал медленно подниматься. Вот он остановился. Железные двери начали со скрипом открываться. И вдруг раздался громкий треск, и лифт с грохотом провалился!\n-2 ел. Жизни.\nБудьте осторожны, если вы потеряете все 10 единиц жизни, вы проиграете!",
  "otvet":[
  ],
  "Hard":-2,
  "hangre":0,
  "root":1
},
{
  "text":"Лифт начал медленно спускаться вниз. Вдруг раздался громкий треск и лифт упал",
  "otvet":[
    {"text":"...","schena":19}
  ],
  "Hard":0,
  "hangre":0,
  "root":1
},

{
  "text":"Терь вы решаете осмотреть свое состояние и двинуться в путь.",
  "otvet":[
    {"text":"открываете дверь с названием «ВЫХОД»","schena":0}
  ],
  "Hard":0,
  "hangre":0,
  "root":1
},
{
  "text":"Терь вы решаете осмотреть свое состояние и двинуться в путь.",
  "otvet":[
    {"text":"открываете дверь с названием «ВЫХОД»","schena":0}
  ],
  "Hard":0,
  "hangre":0,
  "root":1
},
{
  "text":"Терь вы решаете осмотреть свое состояние и двинуться в путь.",
  "otvet":[
    {"text":"открываете дверь с названием «ВЫХОД»","schena":0}
  ],
  "Hard":0,
  "hangre":0,
  "root":1
},

{
  "text":"Терь вы решаете осмотреть свое состояние и двинуться в путь.",
  "otvet":[
    {"text":"открываете дверь с названием «ВЫХОД»","schena":0}
  ],
  "Hard":0,
  "hangre":0,
  "root":1
},
{
  "text":"Терь вы решаете осмотреть свое состояние и двинуться в путь.",
  "otvet":[
    {"text":"открываете дверь с названием «ВЫХОД»","schena":0}
  ],
  "Hard":0,
  "hangre":0,
  "root":1
},
{
  "text":"Терь вы решаете осмотреть свое состояние и двинуться в путь.",
  "otvet":[
    {"text":"открываете дверь с названием «ВЫХОД»","schena":0}
  ],
  "Hard":0,
  "hangre":0,
  "root":1
},

{
  "text":"Терь вы решаете осмотреть свое состояние и двинуться в путь.",
  "otvet":[
    {"text":"открываете дверь с названием «ВЫХОД»","schena":0}
  ],
  "Hard":0,
  "hangre":0,
  "root":1
},
{
  "text":"Вы чудом выжили. Здесь темно, только тусклый свет поврежденного лифта освещал коридор.",
  "otvet":[
  ],
  "Hard":0,
  "hangre":0,
  "root":1
}
]
]
user_m = {}
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
  user_m[message.chat.id]["schena"] = int(str(message.text).split("_")[2])
  user_m[message.chat.id]["root_scena"] = str(message.text).split("_")[1]
  user_m[message.chat.id]["pred_schena"] = True
  message.text = "хех"
  echo_all(message)

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
    elif str(message.text).split("_")[0] == "/teleport.admin":
      teleport_admin(message)
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