import re
pattern = r'[+-]?\d*\.\d+$'
n = int(input())
for _ in range(n):
    s = input()
    print(bool(re.match(pattern, s)))
# for i in re.finditer(pattern, text):
#     print(i.span())
#     print(i.start())
#     print(i.end())

# # first occurence
# print(re.search(pattern, text).start)

# search barlyq stroka
# match basynan
# ex: codemode pattern = 'em'
# search --> Yes
# match --> No tak kak pervye CO 