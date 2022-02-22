from dataclasses import replace
import re
with open('raw.data', 'r', encoding='utf-8') as file:
    text = file.read()
pattern = r'Стоимость\s(\d+ \d+|\d+)'
jeak = re.findall(pattern, text)
sum = 0
for i in jeak:
    i = i.replace(' ', '')
    # print(i)
    i = int(i)
    sum += i
# for i in jeak:
#     if i == len(5):
#         i = i.replace(' ', '')
#         i = int(i)
#         sum += i
#     else:
#         i = int(i)
#         sum += i
print(sum)