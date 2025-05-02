s=input()
cnte=0
cntb=0
for i in range(len(s)-1):
    if s[i:i+2]=="ee":
        cnte+=1
    if s[i:i+2]=="eb":
        cntb+=1
print(cnte,cntb)