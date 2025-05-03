def find_tsn(n):
    while n>0:
        if n%10==3 or n%10==6 or n%10==9:
            return True
        n//=10
    return False

def find(a,b):
    cnt=0
    for i in range(a,b+1):
        if i%3==0 or find_tsn(i):
            cnt+=1
    return cnt

a, b = map(int, input().split())
print(find(a,b))