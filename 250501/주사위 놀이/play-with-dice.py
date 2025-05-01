l=list(map(int,input().split()))
cnt=[0 for _ in range(7)]
for i in l:
    cnt[i]+=1
for i in range(1,7):
    print(f'{i} - {cnt[i]}')