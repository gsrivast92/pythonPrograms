def linersearch (A, key):
	position = 0
	flag = False
	while position < len(A) and not flag:
		if A[position] == key:
			flag = True
		else:
			position = position + 1
	return flag
	
	


m = [4,7,9,15,21]
k = 3	
found = linersearch(m, k)
print("The number",k,"is found : ", found)