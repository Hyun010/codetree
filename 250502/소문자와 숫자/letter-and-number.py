s=list(input())
l=''
for c in s:
    if (c>="A" and c<="Z") or (c>="a" and c<="z") or (c>="0" and c<="9"):
        l+=c.lower()
print(l)