n=int(input())
if n==1:
    print("*")
elif n%2==0:
    for i in range(n):
        if i==0:
            for j in range(n):
                print("*",end=" ")
        else:
            k=n//2-(i//2)
            for j in range(2*(i//2)+1):
                print(" ",end=" ")
            for j in range(k):
                print("*   ",end="")
        print()
else:
    for i in range(n-1):
        if i==0:
            for j in range(n):
                print("*",end=" ")
        else:
            k=n//2-(i//2)
            for j in range(2*(i//2)+1):
                print(" ",end=" ")
            for j in range(k):
                print("*   ",end="")
        print()