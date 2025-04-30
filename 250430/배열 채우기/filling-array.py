l=list(map(int,input().split()))
a=[]
for i in l:
    if i==0:
        break
    else:
        a.append(i)
a.reverse()
print(*a)