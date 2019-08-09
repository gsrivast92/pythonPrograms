#Sum of Natural numbers given by user
a = input("Enter the number for which sum of natural number required :")

for i in range(int(a)):
	i +=i
print("Sum of "+ a + " natural numbers are  :", i) 