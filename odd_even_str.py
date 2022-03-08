
s = '\n'.join([input() for _ in range(int(input()))])
t = s.split()


s1= ''
s2= ''
for k in t:
    for i in range(len(k)):
        if (i % 2 == 0):
            s1 +=k[i]
        else:
            s2 +=k[i]
    print(s1+' '+s2)
    s1=''
    s2=''