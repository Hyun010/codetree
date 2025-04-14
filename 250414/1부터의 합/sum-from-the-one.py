N=int(input())
h=0
for i in range(1,101):
    h+=i
    if h>N:
        print(i)
        break