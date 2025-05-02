def gcd(n,m):
    while m>0:
        n,m=m,n%m
    return n

def lcm(n,m):
    print((n*m)//gcd(n,m))

n, m = map(int, input().split())
lcm(n,m)