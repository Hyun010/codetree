a, b, c, d = map(int, input().split())
t=0
if d-b<0:
    c-=1
    t=60-b+d
else:
    t=d-b
print((c-a)*60+t)