import json

with open('4444.json') as f:
  textMess = json.load(f)
f.close()
root_add = {'ffff':'ffff','444':444}
textMess.append(root_add)

with open('4444.json', 'w') as outfile:
    json.dump(textMess, outfile)
outfile.close()
