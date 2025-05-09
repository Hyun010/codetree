n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m=0
for i in range(n):
    t=nums[i]+nums[2*n-1-i]
    m=max(m,t)
print(m)