a=map(str,input().split())
b=map(str,input().split())
c=map(str,input().split())
l=[]
for p,t in [a,b,c]:
    if p=="Y" and int(t)>=37:
        l.append(p)
if len(l)>=2:
    print("E")
else:
    print("N")