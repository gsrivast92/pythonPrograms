import os
def solve(s):
    t = s.split(' ')
    tmp = []
    for i in t:
        i = i.capitalize()
        tmp.append(i)
        
    str1 = " "
    k = str1.join(tmp)
    return k
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    s = input()

    result = solve(s)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
