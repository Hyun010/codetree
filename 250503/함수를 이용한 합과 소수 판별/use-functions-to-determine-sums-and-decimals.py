def judge(n):
    cnt=1
    for i in range(2,n+1):
        if n%i==0:
            cnt+=1
        if cnt>2:
            return False
    if cnt==2:
        if ((n//10)+(n%10))%2==0:
            return True
        else:
            return False
    else:
        return False

a, b = map(int, input().split())
cnt=0
for i in range(a,b+1):
    if judge(i):
        cnt+=1
print(cnt)