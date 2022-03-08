temp = {'apple' : '2 kg', 'banana' :'3 kg', 'guava' : '4 kg'}
#print(temp)

#Function 1 
#dict.keys() gives all keys
print(temp.keys())

#Function 2
#dict.values()
print(temp.values())

print(temp['apple'])

temp['chiku'] ='5 kg'
print(temp)

temp['apple'] ='1 kg'
print(temp)



#For loop behavior in dictonary
#If we dont write anything then keys will be printed in the for loop
for i in temp:
    print(i)

for i in temp.values():
    print(i)

#if condition

if '1 kg' in temp.values():
    print("We need to buy apple also")

#print value of particular key
#get works on keys
print(temp.get('banana'))



#for k, v we can find keys and values both with the help of .items()

for i, j in temp.items():
    print(i, j)


for i in temp.keys():
    temp[i] = '5 kg'
    print(i)

print(temp)

print(temp['apple'])
#==================================================================================#

#del keyword

lst = ['a', 'b', 'c', 'd']

del lst[0]
print(lst[-2:])
print(lst[-3:])

#Slicing and here it will taking values from -2 to end and end is -1
del lst[-2:]


print(lst)


#dic del operation


dict = {'a':1, 'b':2, 'c':3}


del dict['a']

print(dict)

#\n



if '8 kg' not in temp.values():
    print("We need to buy apple also")



# mutable and immutable

#mutable
lst = [1,2,3,4,5]

# lst[1] = 8

print(lst)


#immutable like tuple

tup = (1,2,3,5)

print(tup)


#concept of pass, break and continue


# while(2 < 24):
#     print("blalalalalla")
#     print('kkkk')


#Concept of end and sep 


#print("This is cat", end='gautrav')

#sep - seperator
#print("Study", "tonight")
print("Study", "tonight", "test" , sep = '<>')




# #
# print("Studytonight", end=' ')
# print("is awesome")