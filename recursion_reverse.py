def reverse(s):
	if len(s) == 0:
		return s
	else:
		return reverse(s[1:]) + s[0]

		


s = input("Input a String :")		
		
		
		
p = reverse(s)
print(p)