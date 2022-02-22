import re
text = '12NUare2345kd3kd'
pattern = r'\d{1,3}'
ls = re.findall(pattern, text)
print(ls)