cnta=0
cntb=0
cntc=0
cntd=0
for _ in range(3):
    s,t=map(str,input().split())
    if s=="Y":
        if int(t)>=37:
            cnta+=1
        else:
            cntc+=1
    else:
        if int(t)>=37:
            cntb+=1
        else:
            cntd+=1
a=[cnta,cntb,cntc,cntd]
if cnta>=2:
    a.append("E")
print(*a)