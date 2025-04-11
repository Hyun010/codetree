B,C=map(int,input().split())
A=[]
A.append(B)
A.append(C)
for _ in range(8):
    A.append((A[-1]+A[-2])%10)
print(*A)