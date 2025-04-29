a,b=map(int,input().split())
l=[i for i in range(b,a-1,-2)]
for i in range(1,10):
    for j in range(len(l)):
        if j==len(l)-1:
            print(f'{l[j]} * {i} = {l[j]*i}',end='')
        else:
            print(f'{l[j]} * {i} = {l[j]*i}',end=' / ')
    print()