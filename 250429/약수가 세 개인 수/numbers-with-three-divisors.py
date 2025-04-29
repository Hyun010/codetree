def find_len(n):
    l=[1]
    for i in range(2,n+1):
        if n%i==0:
            l.append(i)
    return len(l)

start, end = map(int, input().split())
cnt=0
for i in range(start,end+1):
    if find_len(i)==3:
        cnt+=1
print(cnt)