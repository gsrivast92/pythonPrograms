s = input()
t = s.split()
tmp = []
for i in t:
    i = i.capitalize()
    tmp.append(i)
    
str1 = ' '
k = str1.join(tmp)
print(k)