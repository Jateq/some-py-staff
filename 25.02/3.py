import re 
pattern = r'([a-zA-z0-9])\1+'
ans = re.search(pattern, input())
if ans:
    print(ans.group(1))
else:
    print(-1)