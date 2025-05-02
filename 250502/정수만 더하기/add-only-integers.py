s=list(input())
l=[]
for c in s:
    if (c>="0" and c<="9"):
        l.append(int(c))
print(sum(l))