n,m=map(int,input().split())
l=list(map(int,input().split()))
cnt=0
for i in l:
    if i==m:
        cnt+=1
print(cnt)