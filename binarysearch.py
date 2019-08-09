def binarysearch(A, key):
	low = 0 
	high  = len(A)-1
	while low <= high:
		mid = (low+high)//2
		if key == A[mid]:
			return True
		elif key < A[mid]:
			high = mid -1
		else:
			low = mid+1
	return False
			
A = [9,10,20,3,4,23]
key = 27


found = binarysearch(A,key)

print("The element",key, "found in the list :" ,found)

	