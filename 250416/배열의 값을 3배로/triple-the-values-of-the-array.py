l=[list(map(int,input().split())) for _ in range(3)]
for i in range(3):
    for j in range(3):
        l[i][j]*=3
for i in range(3):
    for j in range(3):
        if j!=3:
            print(l[i][j], end=" ")
        else:
            print(l[i][j])
    print()