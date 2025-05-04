def p(n):
    global t
    if n==0:
        return
    print("*"*(t-n))
    p(n-1)

n = int(input())
t=n+1
p(n)