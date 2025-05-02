n=int(input())
h=0
for _ in range(n):
    h+=int(input())
h=str(h)
print(h[1:]+h[0])