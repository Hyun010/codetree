def gcd(a,b):
    while b:
        t=a%b
        a=b
        b=t
    return a

def lcm(a, b):
    return int(a * b / gcd(a, b))

n = int(input())
arr = list(map(int, input().split()))
if n==1:
    print(arr[0])
else:
    l=lcm(arr[0],arr[1])
    for i in range(2,len(arr)):
        l=lcm(l,arr[i])
    print(l)