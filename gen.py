import json

with open('sourse/continuity_convert_Unicod.json') as f:
  textMess = json.load(f)
f.close()

root_add = []
root = int(input("root: "))
for w in range(0,int(input("номер последней сцены: "))+1):
    print("номер: "+str(w))
    print("{")
    text = input("\t\"text\": ")
    print("\t\"otvet\":[")
    otvete = []
    for e in range(0,int(input("количесиво ответов: "))):
        print('{')
        text_otveta = input("\t\t\"text\": ")
        tp = int(input("\t\t\"schena\": "))
        print('}')
        otvete.append({"text":text_otveta,"schena":tp})
    str_hard = input("\t\"Hard\": ")
    if str_hard != '':
        Hard = int(str_hard)
    else:
        Hard = 0
    str_hangre = input("\t\"hangre\": ")
    if str_hangre != '':
        hangre = int(str_hangre)
    else:
        hangre = 0
    print("\t]")
    print("}")
    root_add.append({"text":text,"otvet":otvete,"Hard":Hard,"hangre":hangre,"root":root})

textMess.append(root_add)

with open('continuity_convert_Unicod_add_'+str(root)+'.json', 'w') as outfile:
    json.dump(textMess, outfile)
