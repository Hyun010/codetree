n=int(input())
p=65
for i in range(n):
    for j in range(n):
        print(chr(p),end='')
        p+=1
    print()