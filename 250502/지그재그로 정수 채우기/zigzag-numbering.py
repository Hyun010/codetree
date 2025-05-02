n, m = map(int, input().split())
k=0
l=[[0 for _ in range(m)] for _ in range(n)]
for i in range(m):
    for j in range(n):
        if i%2==0:
            l[j][i]=k
            k+=1
        else:
            l[n-1-j][i]=k
            k+=1
for i in range(n):
    for j in range(m):
        print(l[i][j],end=' ')
    print()