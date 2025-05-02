s,q=map(str,input().split())
for _ in range(int(q)):
    e,a,b=map(str,input().split())
    if e=="1":
        s=list(s)
        i1=int(int(a)-1)
        i2=int(int(b)-1)
        t1=s[i2]
        t2=s[i1]
        s[i1]=t1
        s[i2]=t2
        s="".join(s)
        print(s)
    elif e=="2":
        s=s.replace(a,b)
        print(s)