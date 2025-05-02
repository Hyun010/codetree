l=[list(map(int,input().split())) for _ in range(2)]
for i in range(2):
    s=0
    for j in range(4):
        s+=l[i][j]
    print(f'{s/4:.1f}',end=' ')
print()
for i in range(4):
    s=0
    for j in range(2):
        s+=l[j][i]
    print(f'{s/2:.1f}',end=' ')
print()
s=0
for i in range(2):
    for j in range(4):
        s+=l[i][j]
print(f'{s/8:.1f}')