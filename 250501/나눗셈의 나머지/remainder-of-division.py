a,b=map(int,input().split())
cnt=[0 for _ in range(10)]
while a>1:
    cnt[a%b]+=1
    a=a//b
s=0
for i in cnt:
    if i==0:
        continue
    s+=i**2
print(s)