n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    p=1
    for j in range(a,b+1):
        p*=j
    print(p)