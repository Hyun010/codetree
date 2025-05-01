l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if i<500:
        l1.append(i)
    elif i>500:
        l2.append(i)
print(max(l1),min(l2))