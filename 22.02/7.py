import re
emails = [
    'dsdfs@gmail.com',
    'dfskdjf@kbtu.kz'
]
pattern = r'.+@[a-z]+\.[a-z]+$'
for i in emails:
    if re.match(pattern, i):
        print(f'Email {i} is valid')
    else:
        print('Not valid') 