A,B=map(int,input().split())
answer=[]
answer.append(A)
while A<B:
    if A%2==0:
        A+=3
        answer.append(A)
    else:
        A*=2
        answer.append(A)
if answer[-1]>B:
    answer.pop()
print(*answer)