m1, d1, m2, d2 = map(int, input().split())
p={0:"Mon",1:"Tue",2:"Wed",3:"Thu",4:"Fri",5:"Sat",6:"Sun"}
t=0
t1=0
t2=0
if m1==m2:
    t=d2-d1
    print(p[t%7])
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
        if i<=7:
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
    print(p[((t1-d1+d2+t2)%7)])
