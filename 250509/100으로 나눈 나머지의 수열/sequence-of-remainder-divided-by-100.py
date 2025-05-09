def p(n):
    if n==1:
        return 2
    if n==2:
        return 4
    return (p(n-1)*p(n-2))%100

N = int(input())
print(p(N))