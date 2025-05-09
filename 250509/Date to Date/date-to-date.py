m1, d1, m2, d2 = map(int, input().split())
t1=0
t2=0
if m1==m2 and d1==d2:
    print(1)
elif m1==m2:
    print(d2-d1+1)
else:
    if m1<=7:
        if m1==2:
            t1=28
        elif m1%2==0:
            t1=30
        else:
            t1=31
    else:
        if m1%2==0:
            t1=31
        else:
            t1=30
    for i in range(m1+1,m2):
        if m1<=7:
            if i==2:
                t2+=28
            elif i%2==0:
                t2+=30
            else:
                t2+=31
        else:
            if i%2==0:
                t2+=31
            else:
                t2+=30
    print(t1-d1+1+d2+t2)