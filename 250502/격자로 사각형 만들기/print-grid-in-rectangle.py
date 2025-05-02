n=int(input())
l=[[1]*n for _ in range(n)]
for i in range(1,n):
    for j in range(1,n):
        l[i][j]=l[i-1][j-1]+l[i][j-1]+l[i-1][j]
for i in range(n):
    for j in range(n):
        print(l[i][j],end=' ')
    print()