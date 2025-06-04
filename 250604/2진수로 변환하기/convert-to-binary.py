n = int(input())
d=[]
while True:
    if n<2:
        d.append(n)
        break
    d.append(n%2)
    n//=2
for i in d[::-1]:
    print(i,end="")