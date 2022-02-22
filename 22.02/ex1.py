import re
with open('raw.data', 'r', encoding='utf-8') as file:
    text = file.read()
pattern = r'(БИН) ([0-9]{12})'
bin = re.search(pattern, text).group(2)
print(bin)
