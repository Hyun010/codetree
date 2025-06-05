n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]
a=[0]*n
for b,c in commands:
    for i in range(b-1,c):
        a[i]+=1
print(max(a))