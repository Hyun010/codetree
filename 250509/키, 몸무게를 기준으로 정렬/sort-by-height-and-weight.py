class P:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

n = int(input())
name = []
height = []
weight = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))
l=[]
for m,h,w in zip(name,height,weight):
    l.append(P(m,h,w))
l.sort(key=lambda x:(x.height,-x.weight))
for k in l:
    print(k.name,k.height,k.weight)