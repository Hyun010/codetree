n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
ax=max(segments)[1]
xin=min(segments)[0]
cnt=0
for _ in range(xin,ax+1):
    cnt+=1
a=[0]*(cnt+1)
for c,d in segments:
    for i in range(c,d):
        a[i]+=1
print(max(a))