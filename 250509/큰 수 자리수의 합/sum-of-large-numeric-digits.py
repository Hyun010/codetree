def p(n):
    if n<10:
        return n
    return p(n//10)+(n%10)

a, b, c = map(int, input().split())
print(p(a*b*c))