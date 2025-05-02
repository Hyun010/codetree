s=list(input())
l=[]
for c in s:
    if (c>="A" and c<="Z") or (c>="a" and c<="z"):
        l.append(c.upper())
print("".join(l))