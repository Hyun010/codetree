def p(n):
    global s
    if n==1:
        return 1
    s+=n+p(n-1)
    return s

N = int(input())
s=0
print(p(N))