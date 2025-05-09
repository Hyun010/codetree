n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]
l=[]
for c in str:
    if c[:len(t)]==t:
        l.append(c)
l.sort()
print(l[k-1])