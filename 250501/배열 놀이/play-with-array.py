n,q=map(int,input().split())
l=list(map(int,input().split()))
for _ in range(q):
    p=list(map(int,input().split()))
    e=p.pop(0)
    if e==1:
        print(l[p[0]-1])
    elif e==2:
        try:
            print(l.index(p[0])+1)
        except:
            print(0)
    else:
        for j in range(p[0]-1,p[1]):
            print(l[j],end=' ')
        print()