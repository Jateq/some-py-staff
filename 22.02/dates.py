import re

dates = [
    '32.01.2022',
    '29.01.2023',
    '04.05.2003',
    '22.14.1901',
    '22/11/1901'
]
pattern = '(0[1-9]|[1-2][0-9]|[3][01])[./](0[1-9]|1[0-2])[./](19[0-9]{2}|20[0-1][0-9]|202[0-2])$'
pattern_2 = r'(?P<day>0[1-9]|[1-2][0-9]|[3][01])[./](?P<month>0[1-9]|1[0-2])[./](?P<year>19[0-9]{2}|20[0-1][0-9]|202[0-2])$'
for date in dates:
    if re.match(pattern, date):
        output = re.match(pattern, date).group(0)
        print(output)
        print('Yes')
    else:
        print('No')
    
    