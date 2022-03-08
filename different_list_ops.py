

if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        stg = str(input())
        a=stg.split()
        if (a[0]== 'append'):
            lst.append(int(a[1]))
        elif(a[0]== 'insert'):
            lst.insert(int(a[1]),int(a[2]))
        elif(a[0]== 'print'):
            print(lst)
        elif(a[0]== 'sort'):
            lst.sort()
        elif(a[0]== 'remove'):
            lst.remove(int(a[1]))
        elif(a[0]== 'reverse'):
            lst.reverse()
        elif(a[0]== 'pop'):
            lst.pop()
        

        

