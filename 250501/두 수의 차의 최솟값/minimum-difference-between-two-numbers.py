n=int(input())
l=list(map(int,input().split()))
s=3000
for i in range(n):
    for j in range(i+1,n):
        if l[j]-l[i]<s:
            s=l[j]-l[i]
print(s)