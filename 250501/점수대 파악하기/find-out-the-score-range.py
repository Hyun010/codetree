l=list(map(int,input().split()))
cnt=[0 for _ in range(11)]
for i in l:
    if i==0:
        break
    cnt[i//10]+=1
for i in range(10,0,-1):
    print(f'{i*10} - {cnt[i]}')