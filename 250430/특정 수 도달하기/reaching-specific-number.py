l=list(map(int,input().split()))
a=[]
for i in l:
    if i>=250:
        break
    else:
        a.append(i)
print(f'{sum(a)} {round(sum(a)/len(a),1):.1f}')