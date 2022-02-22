import re
x = 'rtrtyAD@SE DJ Alim jfds JEfe Je 45 jeFca'
y = re.findall('[Ee]*', x)
for i in range(len(y)):
    if y[i] == 'e' or y[i] == 'E':
        print(i+1) # to find the index+1 of (place) letter
# the next line is to find how many times this letter appears
# y = re.findall('[Ee]+', x) the main thing that changed is: asterics to plus sign 
# print(len(y))

# list
print(y)
# email
c = re.findall('\S+?@\S+?', x)
print(c)
# to find the host
k = re.findall('@(\S*)', x)
print(k)