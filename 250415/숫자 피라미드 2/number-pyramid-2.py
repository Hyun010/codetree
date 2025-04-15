N=int(input())
h=1
for i in range(1,N+1):
    for j in range(1,i+1):
        print(h, end=" ")
        h+=1
    for j in range(1,N-i):
        print(" ",end=" ")
    print()