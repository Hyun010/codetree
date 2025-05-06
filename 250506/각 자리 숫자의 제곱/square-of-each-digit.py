def p(n):
    if n<10:
        return n**2
    return p(n//10)+(n%10)**2

N = int(input())
print(p(N))