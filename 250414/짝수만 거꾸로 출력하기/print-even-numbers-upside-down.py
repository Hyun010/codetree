N=int(input())
L=list(map(int,input().split()))
answer=[]
for n in L:
    if n%2==0:
        answer.append(n)

for i in range(len(answer)-1,-1,-1) :
    print(answer[i],end=' ')