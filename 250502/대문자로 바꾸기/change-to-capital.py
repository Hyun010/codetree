l=[list(map(str,input().split())) for _ in range(5)]
for i in range(5):
    for j in range(3):
        l[i][j]=chr(ord(l[i][j])-32)
for i in range(5):
    for j in range(3):
        print(l[i][j],end=' ')
    print()