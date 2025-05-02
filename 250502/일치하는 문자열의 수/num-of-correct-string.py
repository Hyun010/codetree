n,s=map(str,input().split())
n=int(n)
cnt=0
for _ in range(n):
    p=input()
    if p==s:
        cnt+=1
print(cnt)