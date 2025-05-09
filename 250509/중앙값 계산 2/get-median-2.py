n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    if i%2==0:
        t=arr[:i+1]
        t.sort()
        print(t[i//2],end=' ')