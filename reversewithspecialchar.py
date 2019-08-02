str = 'ab!@cde'


#Function to reverse a string
def reverse(s):
	l1 = len(s)//2
	for i in range(l1):
		s[i],s[-i-1]  = s[-i-1],s[i]
	return s
	
	

#Function  to convert a string into List	
def toList(s):
	l=[]
	for i in s:
		l.append(i)
	return l

	
#Function to return a list having only alphabets#
def isAlphabet(s):
	isAlphabet = []
	for i in s:
		if i.isalpha():
			isAlphabet.append(i)
	return isAlphabet


#Function to convert to Special Character#			
def splchar(s):
	alpha=isAlphabet(s)
	rev = reverse(alpha)
	t = toList(str)
	k=0
	for i in range(len(t)):
		if t[i].isalpha():
			t[i] = rev[k]
			k +=1
	return t
	
	
k = splchar(str)
print(k)
	
	
	

	
	
	
	
	
	
	#if str[i].isalpha():
	#	str1= str.replace(str[i],tmp[k])
	#	k +=1
	#str = str[i:]
#print(str1)
	
	


			
