l=[list(map(int,input().split())) for _ in range(4)]
s=0
for i in range(4):
    for j in range(i+1):
        s+=l[i][j]
print(s)