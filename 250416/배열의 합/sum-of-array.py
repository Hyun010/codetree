l=[list(map(int,input().split())) for _ in range(4)]
for i in range(4):
    h=0
    for j in range(4):
        h+=l[i][j]
    print(h)