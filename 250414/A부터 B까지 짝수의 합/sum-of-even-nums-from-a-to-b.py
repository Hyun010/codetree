A,B=map(int,input().split())
h=0
for i in range(A,B+1):
    if i%2==0:
        h+=i
print(h)