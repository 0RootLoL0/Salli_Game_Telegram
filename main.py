#  ":'######:::::'###::::'##:::::::'##:::::::'####:"
#  ":##... ##:::'## ##::: ##::::::: ##:::::::. ##::"
#  ":##:::..:::'##:. ##:: ##::::::: ##:::::::: ##::"
#  ": ######::'##:::. ##: ##::::::: ##:::::::: ##::"
#  ":..... ##: #########: ##::::::: ##:::::::: ##::"
#  "'##::: ##: ##.... ##: ##::::::: ##:::::::: ##::"
#  ". ######:: ##:::: ##: ########: ########:'####:"
#  ":......:::..:::::..::........::........::....::"
#  telegram bot Game text quest
import telebot
import json
from telebot import types
from subprocess import Popen, PIPE
from multiprocessing import Process, Queue
with open('sourse/continuity_convert_Unicod.json') as f:
  textMess = json.load(f)
  f.close()
bot = telebot.TeleBot("qqq")

def db_use(type_rec, rec_w):
  def execute(queue, result_n, rec):
    proc = Popen('python3 sql.py ' + str(result_n) + ' \"' + str(rec) + '\"', shell=True, stdout=PIPE)
    proc.wait()  # дождаться выполнения
    queue.put(proc.communicate()[0])
  queue = Queue()
  p = Process(target=execute, args=(queue, type_rec, rec_w))
  p.start()
  p.join()
  if type_rec == 0:
    return str(queue.get().decode("utf-8")) == ""
  else:
    return json.loads(queue.get().decode('utf-8'))

@bot.message_handler(commands=['statistics_0rootlol0'])
def statistics_0rootlol0(message):
  user_len = db_use(1, "SELECT count(*) FROM users")[0][0]
  bot.send_message(message.chat.id, "количество зарегистрированых Users`:  " + str(user_len))
  print(db_use(0, "UPDATE users SET schena_p=0 WHERE id=" + str(message.chat.id)))

def condition(message):
  hard, hangree = db_use(1, "SELECT hard, hangree FROM users WHERE id="+str(message.chat.id))[0]
  bot.send_message(message.chat.id, "Ед.жизни:  " + str(hard) +
                                  "\nЕд.голода: " + str(hangree))
  print(db_use(0, "UPDATE users SET schena_p=0 WHERE id=" + str(message.chat.id)))

def teleport(id, root, schena, numOtvet):
  schena_r = textMess[root][schena]["otvet"][numOtvet]["schena"]
  root_scena = textMess[root][schena]["root"]
  print(db_use(0, "UPDATE users SET root=" + str(root_scena) + ", schena=" + str(schena_r) + ", schena_p=1 WHERE id=" + str(id)))
  return schena_r, root_scena

@bot.message_handler(commands=['start'])
def send_welcome(message):
  photo = open('sourse/logotypea.png', 'rb')
  bot.send_photo(message.chat.id, photo)
  bot.send_message(message.chat.id, "добро пожаловать")
  markup = types.ReplyKeyboardMarkup(row_width=1)
  markup.row(types.KeyboardButton("1. открыть дверь"))
  bot.send_message(message.chat.id, textMess[0][0]["text"], reply_markup=markup)
  if int(db_use(1, "SELECT COUNT(*) FROM users WHERE id="+str(message.chat.id))[0][0]) != 1:
    print(db_use(0, "INSERT INTO users(id,login) VALUES ("+str(message.chat.id)+",'"+str(message.chat.username)+"')"))
  else:
    db_use(0, "UPDATE users SET root=0, schena=0, schena_p=1, hard=10, hangree=10 WHERE id="+str(message.chat.id))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
  if int(db_use(1, "SELECT COUNT(*) FROM users WHERE id=" + str(message.chat.id))[0][0]) == 1:
    print("if 1 in")
    root, schena, schena_p, hard, hangree = db_use(1, "SELECT root, schena, schena_p, hard, hangree FROM users WHERE id =" + str(message.chat.id))[0]
    if int(schena_p) == 1:
      print("if 2 in")
      hard += textMess[root][schena]["Hard"]
      hangree += textMess[root][schena]["hangre"]

    print(str(message.text).split(".")[0])
    if str(message.text).split(".")[0] == "1":
      schena, root = teleport(message.chat.id, root, schena, 0)
    elif str(message.text).split(".")[0] == "2" and len(textMess[root][schena]["otvet"]) >= 2:
      schena, root = teleport(message.chat.id, root, schena, 1)
    elif str(message.text).split(".")[0] == "3" and len(textMess[root][schena]["otvet"]) >= 3:
      schena, root = teleport(message.chat.id, root, schena, 2)
    elif str(message.text).split(".")[0] == "4" and len(textMess[root][schena]["otvet"]) >= 4:
      schena, root = teleport(message.chat.id, root, schena, 3)
    elif str(message.text).split(".")[0] == "5" and len(textMess[root][schena]["otvet"]) >= 5:
      schena, root = teleport(message.chat.id, root, schena, 4)
    elif str(message.text).split(".")[0] == "9":
      condition(message)
    else:
      bot.send_message(message.chat.id, "error")
      schena_p = 0

    markup = types.ReplyKeyboardMarkup(row_width=len(textMess[root][schena]["otvet"]))

    for otvet in range(0, len(textMess[root][schena]["otvet"])):
        markup.row(types.KeyboardButton(str(otvet + 1) + ". " +textMess[root][schena]["otvet"][otvet]["text"]))
    markup.row(types.KeyboardButton("9. моё состояние"))
    bot.send_message(message.chat.id, textMess[root][schena]["text"], reply_markup=markup)
    db_use(0, "UPDATE users SET schena_p="+str(schena_p)+", hard="+str(hard)+", hangree="+str(hangree)+" WHERE id=" + str(message.chat.id))
  else:
    bot.send_message(message.chat.id, "вы не зарегистриваны для регистрации команда /start")

bot.polling()