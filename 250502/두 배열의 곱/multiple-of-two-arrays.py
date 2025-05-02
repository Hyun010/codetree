l1=[list(map(int,input().split())) for _ in range(3)]
_=input()
l2=[list(map(int,input().split())) for _ in range(3)]
l3=[[0 for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        l3[i][j]=l1[i][j]*l2[i][j]
for i in range(3):
    for j in range(3):
        print(l3[i][j],end=' ')
    print()