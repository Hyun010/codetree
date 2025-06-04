def ten(b):
    n=0
    for i in b:
        n=2*n+int(i)
    return n

def two(b):
    d=[]
    c=''
    while True:
        if b<2:
            d.append(b)
            break
        d.append(b%2)
        b//=2
    for i in d[::-1]:
        c+=str(i)
    return c

N = list(input())
d=ten(N)
d*=17
print(two(d))