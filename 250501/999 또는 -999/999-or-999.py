l=list(map(int,input().split()))
a=[]
for i in l:
    if i==999 or i==-999:
        break
    a.append(i)
print(max(a),min(a))