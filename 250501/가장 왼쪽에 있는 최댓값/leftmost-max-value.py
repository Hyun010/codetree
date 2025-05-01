n = int(input())
a = list(map(int, input().split()))
t=0
l=[]
while True:
    m=max(a)
    t=a.index(m)
    if t==0:
        l.append(t+1)
        break
    l.append(t+1)
    a=a[:t]
print(*l)