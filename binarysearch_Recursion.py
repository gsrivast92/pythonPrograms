#Function to demonstrate Binary search with Recurrsion


def binarysearch(A,key, low,high):
	if low > high:
		return False
		
	else:
		mid = (low+high)//2
		if key == A [mid]:
			return True
		
		elif key < A[mid]:
			return binarysearch(A,key, low, mid-1)
		else:
			return binarysearch(A, key, mid+1, high)
			
	return False
			
A = [9,10,20,23,25]
key = 27
low = 0
high = 4

found = binarysearch(A,key,low, high)

print("The element",key, "found in the list :" ,found)