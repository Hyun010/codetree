class T:
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
for n,h,w in zip(name,height,weight):
    l.append(T(n,h,w))
l.sort(lambda x: x.height)
for s in l:
    print(s.name, s.height, s.weight)