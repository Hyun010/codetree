a,b=map(str,input().split())
a=list(a)
b=list(b)
p1=''
p2=''
for c in a:
    if (c>="0" and c<="9"):
        p1+=c
    else:
        break
for c in b:
    if (c>="0" and c<="9"):
        p2+=c
    else:
        break
print(int(p1)+int(p2))