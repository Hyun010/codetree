N=int(input())
l=[list(map(int,input().split())) for _ in range(N)]
answer=[]
for n,m in l:
    h=0
    for i in range(n,m+1):
        if i%2==0:
            h+=i
    answer.append(h)
for n in answer:
    print(n)
