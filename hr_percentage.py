n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

test = 0
tmp = []
for i in student_marks:
    if (query_name == i):
        tmp = student_marks[i]
        for i in tmp:
            test +=i

final = test/len(tmp)
print ('%.2f'%final)
            
    
