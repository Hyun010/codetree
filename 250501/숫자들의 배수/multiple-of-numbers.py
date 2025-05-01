n=int(input())
l=[]
cnt=0
i=1
while True:
    l.append(n*i)
    if (n*i)%5==0:
        cnt+=1
    if cnt==2:
        break
    i+=1
print(*l)