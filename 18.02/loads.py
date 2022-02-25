import json
file = open('output.json', 'r')
text = file.read()
print(text)
print(type(text))

d = dict()
d = json.loads(text)
print(type(d))
print(d)
for key, v in d.items():
    print(key, v)