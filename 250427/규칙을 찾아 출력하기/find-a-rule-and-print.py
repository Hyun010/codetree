n=int(input())
for i in range(n):
    if i==0 or i==n-1:
        for j in range(n):
            print("*",end=" ")
        if i==0:
            print()
    else:
        for j in range(n):
            if j==0 or j==n-1:
                print("*",end=" ")
            else:
                if i>j:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
        print()