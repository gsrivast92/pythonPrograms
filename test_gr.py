def check_last_pos(nums):
    nums.sort()
    t = nums[-1]
    num = 0
    for i in range(1,t):
        #print(i)
        if i not in nums:
            num = i
            break
        else:
            num = t+1
            if num == 0:
                num +=1
    
    return num

k = check_last_pos([-1, -3])
#print(k)


lst = [-1,-3]
lst.sort()
print(lst[-1])
print(int(lst[-1]))