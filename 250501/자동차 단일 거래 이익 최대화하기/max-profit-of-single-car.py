n = int(input())
price = list(map(int, input().split()))
p=-1
s=0
for i,j in enumerate(price):
    if i==0:
        p=i
    if price[p]>price[i]:
        p=i
    if j-price[p]>s:
        s=j-price[p]
print(s)