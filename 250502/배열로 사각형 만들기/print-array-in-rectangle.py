l=[[1]*5 for _ in range(5)]
for i in range(1,5):
    for j in range(1,5):
        l[i][j]=l[i-1][j]+l[i][j-1]
for i in range(5):
    for j in range(5):
        print(l[i][j],end=' ')
    print()