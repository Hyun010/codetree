N=int(input())
answer=[]
for i in range(1,N+1):
    if i%2==0 or i%3==0 or i%5==0:
        continue
    else:
        answer.append(i)
print(len(answer))