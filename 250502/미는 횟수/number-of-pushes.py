s1=input()
s2=input()
temp=s1
cnt=0
while True:
    if s1==s2:
        print(cnt)
        break
    s1=s1[len(s1)-1]+s1[:len(s1)-1]
    cnt+=1
    if s1==temp:
        print(-1)
        break