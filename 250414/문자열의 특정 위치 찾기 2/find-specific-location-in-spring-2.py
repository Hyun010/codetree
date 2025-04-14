l=["apple", "banana", "grape", "blueberry", "orange"]
h=0
answer=[]
check=input()
for i in range(5):
    if l[i][2]==check or l[i][3]==check:
        answer.append(l[i])
        h+=1
for i in range(len(answer)):
    print(answer[i])
print(h)