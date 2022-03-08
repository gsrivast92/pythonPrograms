



sml=[]
flst = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    sml.append(name)
    sml.append(score)
    flst.append(sml)
    sml = []
    
    
tmp = []
for i in flst:
    tmp.append(i[1])
    
    
min_num = min(tmp)    
while (min_num== min(tmp)):
    tmp.remove(min_num)
second_min = min(tmp)
print(second_min)

tmp_str = []

for j in flst:
    if second_min == j[1]:
        tmp_str.append(j[0])


print(sorted(tmp_str))
        

