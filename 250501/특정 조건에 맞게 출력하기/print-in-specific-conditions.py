l=list(map(int,input().split()))
a=[]
for i in l:
    if i==0:
        break
    elif i%2==0:
        a.append(i//2)
    else:
        a.append(i+3)
print(*a)