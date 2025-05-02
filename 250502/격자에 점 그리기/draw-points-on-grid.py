n,m=map(int,input().split())
l=[[0]*n for _ in range(n)]
k=1
for _ in range(m):
    x,y=map(int,input().split())
    l[x-1][y-1]=k
    k+=1
for i in range(n):
    for j in range(n):
        print(l[i][j],end=' ')
    print()