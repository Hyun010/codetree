class T:
    def __init__(self,name,address,region):
        self.name=name
        self.address=address
        self.region=region

n = int(input())
name = []
street_address = []
region = []
for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)
l=[]
for n,a,r in zip(name,street_address,region):
    l.append(T(n,a,r))
l.sort(lambda x: x.name)
l.reverse()
print(f'name {l[0].name}')
print(f'addr {l[0].address}')
print(f'city {l[0].region}')