from lib2to3.pygram import pattern_symbols
import re
text = '12NUare2345kd3kd'
pattern = r'\d+'
ls = re.findall(pattern, text)
print(ls)