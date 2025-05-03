def judge(n):
    cnt=1
    for i in range(2,n+1):
        if n%i==0:
            cnt+=1
        if cnt>2:
            return False
    if cnt==2:
        return True
    else:
        return False

def find(a,b):
    l=[]
    for i in range(a,b+1):
        if judge(i):
            l.append(i)
    return sum(l)

a, b = map(int, input().split())
print(find(a,b))