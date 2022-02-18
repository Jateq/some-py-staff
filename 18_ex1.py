import json
# dump,dumps
# load, loads
d = {
    "name" : "Bauka",
    "age" : 18,
    'height' : 181
}

# open close
values = json.dumps(d, indent = 8, sort_keys = True)
with open('output.json', 'w') as file:
    file.write(values)
# automatically opens and closes
