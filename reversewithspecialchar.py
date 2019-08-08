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

#Function to convert List to String
def toStr(lst):
		str = ''.join(lst)
		return str
	

#Function to convert to Special Character#			
def splcharReverse(s):
	alpha=isAlphabet(s)
	rev = reverse(alpha)
	temp = toList(str)
	k=0
	for i in range(len(temp)):
		if temp[i].isalpha():
			temp[i] = rev[k]
			k +=1
	tempStr = toStr(temp)
	return tempStr
	

    
    
# Execution code 
str = "a!!!b.c.d,e'f,ghi"
print("Input string: " + str) 
revLst = splcharReverse(str) 
print("Output string: " + revLst)