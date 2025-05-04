import sys
sys.setrecursionlimit(10**6)

def p1(n):
    if n==0:
        return
    print(n,end=' ')
    n-=1
    p1(n)

def p2(n):
    global t
    if n==0:
        return
    print(t-n,end=' ')
    n-=1
    p2(n)

n = int(input())
t=n+1
p2(n)
print()
p1(n)