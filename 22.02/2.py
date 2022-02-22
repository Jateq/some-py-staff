import re
text = """abbabaabab5bb
        53abjnbjfsfab"""
pattern = 'ab'
ls = re.findall(pattern, text)
print(len(ls))
les = r'\d\d' # two digits
lese = re.findall(les, text)
print(lese)