n=int(input())
l=list(map(float,input().split()))
ag=round(sum(l)/n,1)
print(ag)
if ag>=4:
    print("Perfect")
elif ag>=3:
    print("Good")
else:
    print("Poor")