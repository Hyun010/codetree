n = int(input())
sequence = list(map(int, input().split()))
l=sorted(sequence)
a=[0 for i in range(n)]
for i,s in enumerate(l,start=1):
    t=sequence.index(s)
    sequence[t]=0
    a[t]=i
print(*a)
