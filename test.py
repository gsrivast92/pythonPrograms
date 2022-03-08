if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lst = []
    biglst = []
    t = 0
    tmp = []

    for a in range(0,x+1):
        for b in range(0,y+1):
            for c in range(0,z+1):
                lst.append(a)
                lst.append(b)
                lst.append(c)
                biglst.append(lst)
                lst = []
    s = biglst[:]

                
    for i in biglst:
        k =0
        for j in i:
            k +=j

        if (n == k):
            s.remove(i)
    print(s)


