l=[map(int,input().split()) for _ in range(4)]
for i in range(4):
    s=0
    for j in l[i]:
        s+=j
    print(s)