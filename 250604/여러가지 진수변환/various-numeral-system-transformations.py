N, B = map(int, input().split())
d=[]
while True:
    if N<B:
        d.append(N)
        break
    d.append(N%B)
    N//=B
for i in d[::-1]:
    print(i,end="")