def process(arr,m):
    s=0
    while m>=1:
        s+=arr[m-1]
        if m%2==1:
            m-=1
        else:
            m//=2
    return s

n, m = map(int, input().split())
A = list(map(int, input().split()))
print(process(A,m))