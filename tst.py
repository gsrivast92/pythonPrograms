def check_sum(nums, k):   
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            print(i,j)
            if nums[i] + nums[j] == k:
                count +=1
    return count
num = [1,2,3,4]
k = 4

t= check_sum(num,k)
print(t)


for m in range(1,5):
    print(m)