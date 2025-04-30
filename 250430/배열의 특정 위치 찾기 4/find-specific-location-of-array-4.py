l=list(map(int,input().split()))
a=[]
for i in l:
    if i==0:
        break
    else:
        if i%2==0:
            a.append(i)
print(len(a),sum(a))