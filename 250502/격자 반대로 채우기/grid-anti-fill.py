n=int(input())
k=1
l=[[0]*n for _ in range(n)]
for i in range(n-1,-1,-1):
    if n%2==1:
        if i%2==0:
            for j in range(n-1,-1,-1):
                l[j][i]=k
                k+=1
        else:
            for j in range(n):
                l[j][i]=k
                k+=1
    else:
        if i%2==1:
            for j in range(n-1,-1,-1):
                l[j][i]=k
                k+=1
        else:
            for j in range(n):
                l[j][i]=k
                k+=1
for i in range(n):
    for j in range(n):
        print(l[i][j],end=' ')
    print()