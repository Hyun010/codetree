n=int(input())
p=65
for i in range(n):
    for j in range(i+1):
        if p==91:
            p=65
        print(chr(p),end='')
        p+=1
    print()