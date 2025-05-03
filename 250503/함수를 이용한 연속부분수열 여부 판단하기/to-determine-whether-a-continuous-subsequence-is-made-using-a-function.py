def judge(a,b):
    for i in range(len(a)):
        if a[i:i+len(b)]==b:
            return True
    return False

n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if judge(a,b):
    print("Yes")
else:
    print("No")