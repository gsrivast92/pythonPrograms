s = input()


for i in s:
    flag = "True"
    if i.isalnum():
        flag = flag
        break
    else:
        flag = "False"
print(flag)

for i in s:
    flag = "True"
    if i.isalpha():
        flag = flag
        break
    else:
        flag = "False"
print(flag)

for i in s:
    flag = "True"
    if i.isdigit():
        flag = flag
        break
    else:
        flag = "False"
print(flag)

for i in s:
    flag = "True"
    if i.islower():
        flag = flag
        break
    else:
        flag = "False"
print(flag)


for i in s:
    flag = "True"
    if i.isupper():
        flag = flag
        break
    else:
        flag = "False"
print(flag)


