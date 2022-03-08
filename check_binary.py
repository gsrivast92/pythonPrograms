# a = 13
# b = 7

# sum = a+b
# print(sum)


# bin1 = bin(a)
# bin2 = bin(b)

# #sumt = int(bin1(a)+int(bin(b))

# integer_sum = int(bin1, 2) + int(bin2, 2)
# print(integer_sum)

# print(bin(integer_sum))

a = [3,4,5,3,7]
b = a[:]
t = len(a)
#print(t)
count = 0
for i in range(t):
    del b[i]
    k = len(b)
    lst = []
    final = 0
    
    print(b)
    for j in range(0, k,2):
        if (b[j] < b[j+1]):
    
    b = a[:]

print(count)


