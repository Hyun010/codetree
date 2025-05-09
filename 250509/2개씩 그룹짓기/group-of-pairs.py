n = int(input())
nums = list(map(int, input().split()))
nums.sort()
l=[]
for i in range(n//2+1):
    l.append(nums[i]+nums[-(i+1)])
print(max(l))