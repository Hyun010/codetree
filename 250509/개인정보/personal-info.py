class P:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

n = 5
name = []
height = []
weight = []
for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))
l=[]
for m,h,w in zip(name,height,weight):
    l.append(P(m,h,w))
l.sort(key=lambda x: x.name)
print("name")
for k in l:
    print(k.name,k.height,k.weight)
l.sort(key=lambda x: -x.height)
print()
print("height")
for k in l:
    print(k.name,k.height,k.weight)