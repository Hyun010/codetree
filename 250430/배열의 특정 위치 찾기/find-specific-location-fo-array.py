l=list(map(int,input().split()))
s=0
a=[]
for i in range(10):
    if (i+1)%2==0:
        s+=l[i]
    if (i+1)%3==0:
        a.append(l[i])
print(f'{s} {round(sum(a)/len(a),1):.1f}')