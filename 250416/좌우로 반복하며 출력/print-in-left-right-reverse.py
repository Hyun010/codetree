N=int(input())
l=[]
for i in range(1,N+1):
    l.append(i)
for i in range(N):
    if i%2==0:
        print(*l,sep="")
    else:
        l.reverse()
        print(*l,sep="")
        l.reverse()