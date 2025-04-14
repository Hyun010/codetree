l=[]
for _ in range(10):
    l.append(int(input()))
t=0
f=0
for n in l:
    if n%3==0:
        t+=1
    if n%5==0:
        f+=1
print(t,f)