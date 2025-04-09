A,B=map(int,input().split())
answer=[]
if A<B:
    answer.append(1)
else:
    answer.append(0)
if A==B:
    answer.append(1)
else:
    answer.append(0)
print(answer[0],answer[1])