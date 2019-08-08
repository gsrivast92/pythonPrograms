#Sorting number without sort function

data_list= ['1','6','5','2','-1','2']

#Arbitrary Number 


sorted_list = []


while data_list:
	smallest_num= data_list[0]
	for i in data_list:
		if i < smallest_num:
			smallest_num = i
	sorted_list.append(smallest_num)
	data_list.remove(smallest_num)
print(sorted_list)
