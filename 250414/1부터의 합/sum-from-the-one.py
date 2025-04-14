N=int(input())
h=0
for i in range(1,101):
    if N==1:
        print(1)
        break
    h+=i
    if h>N:
        print(i)
        break