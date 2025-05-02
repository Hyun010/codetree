def gcd(a,b):
    while b>0:
        a,b=b,a%b
    print(a)

n, m = map(int, input().split())
gcd(n,m)