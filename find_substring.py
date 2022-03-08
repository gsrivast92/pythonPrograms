# s = "abcdabcdabcd"
# ft = 0
# secft = 0
# str = "abc"
# count = 0
# sec = len(str)
# print(sec)
# for i in range(len(s)):
#     print(s[i:sec])
#     if s[i:sec] == str:
#         print("good")
#         count +=1
#     sec += 1
# print(count)



string = "Avyaan Avyaan Avyaan Avyaan Avyaan Avyaan Avyaan Avyaan cat my cat dog is black dog is black dog is black" 
sub_string = "dog"



def count_substring(string, sub_string):
    ft = 0
    secft = 0
    count = 0
    sec = len(sub_string)
    
    for i in range(len(string)):
        if string[i:sec] == sub_string:
            count +=1
        sec += 1
    print("Hey word dog came %s times" %(count))
    return count
    
    
    
test_str = "this is the best kit which i can get i am happy for the same"

def count_char(string):
    string = string.split()
    temp_dict = {}
    for i in string:
        if(( i not in temp_dict.keys()) && (i == "  " )):
            temp_dict[i] = 1
        else:
            temp_dict[i] = temp_dict[i]+1
    return temp_dict 

    
    
#count_substring(string, sub_string)

a = count_char(test_str)
print(a)



        
        
        
        