n=int(input())
s=0
a=0
for _ in range(n):
    w=input()
    s+=len(w)
    if w[0]=='a':
        a+=1
print(s,a)