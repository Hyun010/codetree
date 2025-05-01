a,b=map(int,input().split())
l=[0 for _ in range(10)]
l[0]=a
l[1]=b
for i in range(2,10):
    l[i]=(l[i-2]+l[i-1])%10
print(*l)