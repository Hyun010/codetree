n=int(input())
s=list(input().replace(' ',''))
while s!=[]:
    p=''
    for _ in range(5):
        p+=s.pop(0)
        if s==[]:
            break
    print(p)
