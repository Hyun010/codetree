def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

n, m = map(int, input().split())
n,m=swap(n,m)
print(n,m)