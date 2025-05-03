def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def prod(a,b):
    return a*b

def devide(a,b):
    return a//b

a, o, c = input().split()
a = int(a)
c = int(c)
if o=='+':
    print(f'{a} + {c} = {plus(a,c)}')
elif o=='-':
    print(f'{a} - {c} = {minus(a,c)}')
elif o=='*':
    print(f'{a} * {c} = {prod(a,c)}')
elif o=='/':
    print(f'{a} / {c} = {devide(a,c)}')
else:
    print("False")