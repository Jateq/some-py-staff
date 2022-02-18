# JSON - javascript object notation 
import json
# dump,dumps
# load, loads
d = {
    "name" : "Bauka",
    "age" : 19
}

# open close
values = json.dumps(d, indent = 8, sort_keys = True)
# values = json.dumps(d, indent = 8, sort_keys = True, separators=("/", '?'))
print(values)  
# alway we can use dumps
# r and w modes
file = open('output.json', 'w')
file.write(values)
file.close()