s1=input()
s2=input()
cnt=0
for i in range(len(s1)-len(s2)+1):
    if s1[i:i+len(s2)]==s2:
        cnt+=1
print(cnt)