def p(n):
    if n==0:
        return
    print("* "*n)
    p(n-1)
    print("* "*n)

n = int(input())
p(n)