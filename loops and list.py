'''
What is range function.
range function is basically a functions which yields values from 0 to n-1
'''




#How many times this loop will run, and what are values which it will print.
for i in range(10):
    print(i)
    
    
    
    
#While loop
i = 0
while (i < 20 ):
    print("This loop is working")
    print(i)
    i = i+1

    
'''
List Methods


# list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
    
    list = ['gaurav', 'avaya', 'hotmail']
    
    lst.append('avayaan')
    
    
# list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
    
    
    if you want to insert at ex 2 2222
    
    fruits.insert(5, 'papaya')
    
    
# list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
    
    fruits
    lst 
    
    we want to concatenate the lists lst.extend(fruits)
    
# list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
    
    fruits.index('apple')  ===== index element of apple
    
    
# list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
    
    fruits.remove('apple')
    lst.remmove('avaya')
    
    
    
# list.sort() -- sorts the list in place (does not return it). (The sorted() function shown later is preferred.)
    
    lst.sort()
    
# list.reverse() -- reverses the list in place (does not return it)
    
    
# list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
    
    
    if the index is not given it takes out the last element 
    ifi index iis  given it is giving the index element.


List Building
    
>>> a = []
>>> a.append('Tiger')
>>> print(a)
['Tiger']
>>> a.append('Lion')
>>> print(a)
['Tiger', 'Lion']
    
    
    
    
List slicing 
    
    >>> print(a[0:1])
    ['Tiger']
    >>> print(a[0:2])
    ['Tiger', 'Lion']
    >>> print(a[0:3])
    ['Tiger', 'Lion', 'Cat']
    >>> print(a[1:3])
    ['Lion', 'Cat']
    >>> print(a[2:3])
    ['Cat']
    >>> print(a[2:])
    ['Cat']
    >>> print(a[:])
    ['Tiger', 'Lion', 'Cat']
    >>> print(a[:-1])
    ['Tiger', 'Lion']
    >>> print(a[-1:])
    ['Cat']
    >>> print(a[-1:-3])
    []
    >>> print(a[-1:-2])
    []
    >>> print(a[-2:])
    ['Lion', 'Cat']
    >>> print(a[-3:])
    ['Tiger', 'Lion', 'Cat']
    >>> 
    
    
    
>>> 
    




'''