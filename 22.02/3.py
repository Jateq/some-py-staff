import re
text = """abbAAAAADabaabab5bb
        53abjnbjfsfab"""
pattern = '.'
ls = re.findall(pattern, text)
print(len(ls))
les = r'[a-zA-Z]'
lese = re.findall(les, text)
print(lese)