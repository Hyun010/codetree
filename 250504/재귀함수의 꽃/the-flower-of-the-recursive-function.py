def p(n):
    if n==0:
        return
    print(n,end=' ')
    p(n-1)
    print(n,end=' ')

N = int(input())
p(N)