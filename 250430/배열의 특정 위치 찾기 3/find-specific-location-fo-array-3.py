l=list(map(int,input().split()))
a=[]
for i in l:
    if i==0:
        break
    else:
        a.append(i)
print(a[-1]+a[-2]+a[-3])