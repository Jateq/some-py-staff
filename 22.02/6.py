import re
# search and match finding first occurance
# search on all string
# from the beginning of the string
# '$' ends with
# '^' starts with
text = """zabbabaabab5bb
        53abjnbjfsfab""" 
# [] its for or 
pattern = r'[abefgh]+'
print(re.search(pattern, text))
print(re.match(pattern, text))

for i in re.finditer(pattern, text):
    print(i.span())
    print(i.start())
    print(i.end())

# first occurence
print(re.search(pattern, text).start)