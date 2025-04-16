N=int(input())
l=[[0 for _ in range(N)] for _ in range(N)]
m=[]
for i in range(1,N+1):
    m.append(i)
for i in range(N):
    if i%2==0:
        for j in range(N):
            l[j][i]=m[j]
    else:
        index=0
        for j in range(N-1,-1,-1):
            l[j][i]=m[index]
            index+=1
for i in range(N):
    for j in range(N):
        print(l[i][j],end='')
    print()