N,M=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
m=[list(map(int,input().split())) for _ in range(N)]
answer=[[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if l[i][j]==m[i][j]:
            answer[i][j]=0
        else:
            answer[i][j]=1
for i in range(N):
    for j in range(M):
        if j!=M:
            print(answer[i][j],end=" ")
        else:
            print(answer[i][j])
    print()