def process(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s

n = int(input())
print(process(n)//10)