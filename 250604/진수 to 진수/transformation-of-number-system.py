def ten(b,c):
    n=0
    for i in b:
        n=c*n+int(i)
    return n

def two(b,e):
    d=[]
    c=''
    while True:
        if b<e:
            d.append(b)
            break
        d.append(b%e)
        b//=e
    for i in d[::-1]:
        c+=str(i)
    return c

a, b = map(int, input().split())
n = input()
n=list(n)
p=ten(n,a)
print(two(p,b))