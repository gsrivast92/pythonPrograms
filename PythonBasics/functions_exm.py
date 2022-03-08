   
#Functions


# a = 3
# b = 4
# c = a+b

#6 and 7 so now a is 6 and b is 7 

a = 6
# b = 7
# c = a+b

# Functions 


#this is global
t = "This is the the string"
def add(a,b,d):
    #the variable c is local (only inside the function)
    c = a+b+d
    return c

print(t)
#This is add name function which takes two parameters and returns the value as c, This functions takes only 
#two parameters

temp = add(4,5,7)
#k = add(8,9)
print(temp)
#print(k)

def subst(a,b):
    c = a-b
    print(c)

subst(9,4)


def strfunc(str):
    #s = str[-2:]
    t = len(str)
    return t


k = strfunc("This is the string")
print(k)



str = "This is the firts string"
for i in range(len(str)):
    t = len(str)-i
    print(t)
    print(str[t-1])

