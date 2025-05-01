n = int(input())
nums = list(map(int, input().split()))
a=[]
c=[]
for i in nums:
    if i not in a:
        a.append(i)
    else:
        if i not in c:
            c.append(i)
d=list(set(a)-set(c))
if d:
    print(max(d))
else:
    print(-1)