import json
import random

l = list()
with open('names.txt','r') as names:
    for name in names.read().split():
        l.append(name)
d = dict()
for i in range(len(l)):
    d[i+1] = (l[i], random.randint(1, 500))



tex = json.dumps(d, indent=4)

with open('name_out.json','w') as file:
    file.write(tex)