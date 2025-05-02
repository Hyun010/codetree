n,m=map(int,input().split())
l=[[0 for _ in range(m)] for _ in range(n)]
k=1
for i in range(n):
    for j in range(m):
        l[i][j]=k
        k+=1
for i in range(n):
    for j in range(m):
        print(l[i][j],end=' ')
    print()