n=int(input())
cnt=0
s=0
l=[]
for _ in range(n):
    l.append(input())
c=input()
for w in l:
    if w[0]==c:
        cnt+=1
        s+=len(w)
print(f'{cnt} {round(s/cnt,2):.2f}')