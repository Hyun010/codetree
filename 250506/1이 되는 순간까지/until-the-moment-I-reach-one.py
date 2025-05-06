def p(n):
    if n==1:
        return 0
    if n%2==0:
        n//=2
    else:
        n//=3
    return p(n)+1

N = int(input())
print(p(N))