def p(n):
    if n==0:
        return
    print("HelloWorld")
    n-=1
    p(n)

n = int(input())
p(n)