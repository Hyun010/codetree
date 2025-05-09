def p(n):
    if n==1:
        return 0
    if n%2==0:
        n//=2
        return p(n)+1
    else:
        n=n*3+1
        return p(n)+1

n = int(input())
print(p(n))