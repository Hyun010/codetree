def find_n(n):
    l=[1]
    for i in range(2,n):
        if n%i==0:
            l.append(i)
    if sum(l)==n:
        return 1
    return 0

start, end = map(int, input().split())
l=[]
for i in range(start,end+1):
    if find_n(i)==1:
        l.append(i)
print(len(l))