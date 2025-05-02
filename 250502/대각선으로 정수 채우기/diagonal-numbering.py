n, m = map(int, input().split())
k=1
l=[[0 for _ in range(m)] for _ in range(n)]
for p in range(n+m-1):
    for i in range(n):
        j=p-i
        if 0<=j<m:
            l[i][j]=k
            k+=1
for i in range(n):
    for j in range(m):
        print(l[i][j],end=' ')
    print()