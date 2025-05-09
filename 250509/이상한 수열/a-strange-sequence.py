def p(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return p(n//3)+p(n-1)

N = int(input())
print(p(N))