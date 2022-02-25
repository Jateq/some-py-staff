import json
from os import sep
file = open('task.json', 'r')
text = file.read()
d = json.loads(text)
file.close()
d["myName"] = "Temirlan"
d['nums'] = sorted(d['nums'])
d["heroes"]["spider man"] = "Peter" 
values = json.dumps(d, indent=5, sort_keys=True)
file = open('task.json', 'w')
file.write(values)
file.close()