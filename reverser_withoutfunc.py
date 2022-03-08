str = "This is the firsts string"
new=''

for i in range(len(str)):
    t = len(str)-i
    #print(t)
    #print(str[t-1])
    new += str[t-1]
print(new)
