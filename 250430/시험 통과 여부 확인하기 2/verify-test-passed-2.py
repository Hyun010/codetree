n=int(input())
cnt=0
for _ in range(n):
    l=list(map(int, input().split()))
    avg=sum(l)/len(l)
    if avg>=60:
        print("pass")
        cnt+=1
    else:
        print("fail")
print(cnt)