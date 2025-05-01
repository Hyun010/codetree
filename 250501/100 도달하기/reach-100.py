n=int(input())
l=[1,n]
i=2
while True:
    if l[i-2]+l[i-1]>100:
        l.append(l[i-2]+l[i-1])
        break
    l.append(l[i-2]+l[i-1])
    i+=1
print(*l)