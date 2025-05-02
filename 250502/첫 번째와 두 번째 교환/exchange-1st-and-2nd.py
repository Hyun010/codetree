l=list(input())
c1=l[0]
c2=l[1]
for i in range(len(l)):
    if l[i]==c1:
        l[i]=c2
    elif l[i]==c2:
        l[i]=c1
print("".join(l))