l=[list(map(int,input().split())) for _ in range(3)]
input()
m=[list(map(int,input().split())) for _ in range(3)]
answer=[[0 for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        answer[i][j]=l[i][j]*m[i][j]
for i in range(3):
    for j in range(3):
        if j!=3:
            print(answer[i][j], end=" ")
        else:
            print(answer[i][j])
    print()