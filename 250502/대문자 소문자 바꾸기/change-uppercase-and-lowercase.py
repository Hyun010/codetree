s=list(input())
l=''
for c in s:
    if (c>="A" and c<="Z"):
        l+=c.lower()
    elif (c>="a" and c<="z"):
        l+=c.upper()
print(l)