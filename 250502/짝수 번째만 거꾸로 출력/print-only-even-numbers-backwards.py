s=list(input())
a=''
for i in range(len(s)):
    if i%2==1:
        a+=s[i]
print(a[::-1])