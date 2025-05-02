A = input()
B = input()
flag=False
while flag==False:
    if B in A:
        A=A[:A.index(B)]+A[A.index(B)+len(B):]
    else:
        print(A)
        flag=True