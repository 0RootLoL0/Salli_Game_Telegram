import json
with open('continuity_convert_Unicod.json') as f:
    textMess = json.load(f)
    f.close()

for w in textMess[1]:
    print(w["text"])
    print("5555555555555555555555555")
    for e in w['otvet']:
        print(e['text'])
        print(e["schena"])

    print("_________________________")