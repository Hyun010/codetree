def f(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return f(n-2)+f(n-1)

N = int(input())
print(f(N))
