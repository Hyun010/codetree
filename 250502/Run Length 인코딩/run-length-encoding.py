A = list(input())
c=A[0]
cnt=1
s=''
for i in range(1,len(A)):
    if A[i]==c:
        cnt+=1
    else:
        s+=f'{c}{cnt}'
        c=A[i]
        cnt=1
    if i==len(A)-1:
        s+=f'{c}{cnt}'
print(len(s))
print(s)