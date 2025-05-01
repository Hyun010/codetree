n = int(input())
a = list(map(int, input().split()))
m=min(a)
cnt=0
for i in a:
    if i==m:
        cnt+=1
print(m,cnt)