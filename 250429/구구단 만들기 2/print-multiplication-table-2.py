a,b=map(int,input().split())
l=[i for i in range(b,a-1,-1)]
p=[2,4,6,8]
for i in range(4):
    for j in range(len(l)):
        if j==len(l)-1:
            print(f'{l[j]} * {p[i]} = {l[j]*p[i]}',end='')
        else:
            print(f'{l[j]} * {p[i]} = {l[j]*p[i]}',end=' / ')
    print()