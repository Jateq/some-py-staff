import re
ls = list()
pattern = r'[789][0-9]{9}$'
amount = int(input()) - 1
for i in range(amount):
    x = input()
    ls.append(x)
ans = re.search(pattern, input())
for i in ls:
    if ans:
        print("YES")
    else:
        print("NO")