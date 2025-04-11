A=[2,5]
for _ in range(8):
    A.append((A[-1]+A[-2])%10)
print(*A)