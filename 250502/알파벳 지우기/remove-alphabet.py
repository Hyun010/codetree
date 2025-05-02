s1=list(input())
s2=list(input())
p1=''
p2=''
for c in s1:
    if (c>="0" and c<="9"):
        p1+=c
for c in s2:
    if (c>="0" and c<="9"):
        p2+=c
print(int(p1)+int(p2))