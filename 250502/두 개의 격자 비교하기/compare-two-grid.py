n,m=map(int,input().split())
l1=[list(map(int,input().split())) for _ in range(n)]
l2=[list(map(int,input().split())) for _ in range(n)]
l3=[[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if l1[i][j]!=l2[i][j]:
            l3[i][j]=1
        else:
            l3[i][j]=0
for i in range(n):
    for j in range(m):
        print(l3[i][j],end=' ')
    print()