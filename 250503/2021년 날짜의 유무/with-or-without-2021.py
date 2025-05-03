def judge(m,d):
    if 1<=m<=7:
        if m==2:
            if 1<=d<=28:
                return True
            else:
                return False
        elif m%2==1:
            if 1<=d<=31:
                return True
            else:
                return False
        else:
            if 1<=m<=30:
                return True
            else:
                return False
    elif 8<=m<=12:
        if m%2==0:
            if 1<=m<=31:
                return True
            else:
                return False
        else:
            if 1<=m<=30:
                return True
            else:
                return False
    else:
        return False

M, D = map(int, input().split())
if judge(M,D):
    print("Yes")
else:
    print("No")