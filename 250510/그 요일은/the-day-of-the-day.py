m1, d1, m2, d2 = map(int, input().split())
A = input()
p1={"Mon":0,"Tue":1,"Wed":2,"Thu":3,"Fri":4,"Sat":6,"Sun":6}
cnt=0
t1=0
t2=0
if m1==m2 and d1==d2:
    if A=="Mon":
        print(1)
    else:
        print(0)
elif m1==m2:
    if d2-d1==7:
        if (d2-d1)%7==p1[A]:
            print(2)
        else:
            print(1)
    elif d2-d1<7:
        if (d2-d1)%7>=p1[A]:
            print(1)
        else:
            print(0)
    else:
        cnt=(d2-d1)//7
        if (d2-d1)%7>=p1[A]:
            print(cnt+1)
        else:
            print(cnt)
else:
    if m1>=7:
        if m1==2:
            t1=29
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
        if i<=7:
            if i==2:
                t2+=29
            elif i%2==0:
                t2+=30
            else:
                t2+=31
        else:
            if i%2==0:
                t2+=31
            else:
                t2+=30
    cnt=(t1-d1+d2+t2)//7
    if (t1-d1+d2+t2)%7>=p1[A]:
        print(cnt+1)
    else:
        print(cnt)