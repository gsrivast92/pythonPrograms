n = int(input())
arr = map(int, input().split())
lst = list(arr)
max_num = max(lst)
while(max_num == max(lst)):
    lst.remove(max_num)
second_max = max(lst)
print(second_max)




    