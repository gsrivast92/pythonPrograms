#Sorting number without sort function

data_list= ['1','6','5','2','-1','2']

#Arbitrary Number 
smallest_num= data_list[0]

sorted_list = []


while data_list:
	for i in data_list:
		if i < smallest_num:
			i = smallest_num
	sorted_list = 