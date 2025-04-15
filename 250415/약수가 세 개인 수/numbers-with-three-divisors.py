def cnt(n):
    c=1
    for i in range(2,n+1):
        if n%i==0:
            c+=1
    return c

start, end = map(int, input().split())
h=0
for i in range(start,end+1):
   if cnt(i)==3:
    h+=1
print(h) 
