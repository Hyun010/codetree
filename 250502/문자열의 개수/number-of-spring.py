cnt=0
i=1
l=[]
while True:
    s=input()
    if s=="0":
        break
    cnt+=1
    if i%2==1:
        l.append(s)
    i+=1
print(cnt)
for i in range(len(l)):
    print(l[i])