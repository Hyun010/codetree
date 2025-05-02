a,b=map(int,input().split())
c=str(a+b)
cnt=0
for w in c:
    if w=="1":
        cnt+=1
print(cnt)