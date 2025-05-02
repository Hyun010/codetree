n=int(input())
s=0
a=0
for _ in range(n):
    w=input()
    s+=len(w)
    a+=w.count('a')
print(s,a)