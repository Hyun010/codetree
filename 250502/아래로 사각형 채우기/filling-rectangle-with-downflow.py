n=int(input())
k=1
l=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        l[j][i]=k
        k+=1
for i in range(n):
    for j in range(n):
        print(l[i][j],end=' ')
    print()