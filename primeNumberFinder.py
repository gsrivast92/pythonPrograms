a = input("Enter a number : ")
num = int(a)
if num > 1:
	for i in range(2, num):
		print(i)
		if (num % i )==0:	
			print(a,"is not prime number")
			print(i,"times",num//i,"is",num)
			break
		else:
			print(a, "number is a prime number")
		