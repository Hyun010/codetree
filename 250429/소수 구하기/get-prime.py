def find_n(n):
    l=[1]
    for i in range(2,n+1):
        if n%i==0:
            l.append(i)
        if len(l)>=3:
            break
    if len(l)==2:
        return 1
    return 0

n=int(input())
for i in range(1,n+1):
    if find_n(i)==1:
        print(i,end=' ')