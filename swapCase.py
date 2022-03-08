def swap(s):
    p =""
    for i in s:
        if i.isupper():
            p += i.lower()
        elif i.islower():
            #p =s.replace('i', i.upper())
            p += i.upper()
        else:
            p += i
    return p


m = "This is the string"
t = swap(m)
print(t)