m=int(input())
if m<=7:
    if m%2==1:
        print(31)
    elif m==2:
        print(28)
    else:
        print(30)
else:
    if m%2==0:
        print(31)
    else:
        print(30)