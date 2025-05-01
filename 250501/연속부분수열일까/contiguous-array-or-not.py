n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
for i,j in enumerate(l1):
    if j==l2[0]:
        if l1[i:i+len(l2)]==l2:
            print("Yes")
            break
else:
    print("No")