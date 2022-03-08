s = 1011000
t = str(s)
m = len(t)
count =0
p = {}
for i in range(m):
    count = 0
    if t[i] == "1": 
        f = "f"+'_'+ str(i)
        for j in range(i+1, m):     
            if t[j] == "0":
                print("done", t[j])
                count +=1
                p[f]=count
            else:
                break
u = max(p)
final = p[u]
       
print(final)