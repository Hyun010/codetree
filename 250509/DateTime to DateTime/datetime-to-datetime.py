a, b, c = map(int, input().split())
if b<11:
    print(-1)
else:
    t1=0
    t2=0
    if c<11:
        b-=1
        t1=60
    if b<11:
        a-=1
        t2=24*60
    print(((a-11)*24*60)+(t2+(b*60)-(11*60))+(t1+c-11))