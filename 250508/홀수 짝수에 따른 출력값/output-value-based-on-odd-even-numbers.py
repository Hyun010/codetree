def p(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n%2==0:
        return p(n-2)+n
    else:
        return p(n-2)+n

N = int(input())
print(p(N))