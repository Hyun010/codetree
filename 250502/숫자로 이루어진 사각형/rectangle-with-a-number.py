def drawing(n):
    k=1
    for i in range(n):
        for j in range(n):
            if k==10:
                k=1
            print(k,end=' ')
            k+=1
        print()

n = int(input())
drawing(n)