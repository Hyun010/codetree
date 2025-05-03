n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]
for q in queries:
    a,b=q[0],q[1]
    s=0
    for i in range(a-1,b):
        s+=arr[i]
    print(s)