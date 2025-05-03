def judge_yoon(y):
    if y%4==0:
        if y%100==0 and y%400!=0:
            return False
        else:
            return True
    else:
        return False

def judge(y,m,d):
    if 1<=m<=7:
        if m==2 and judge_yoon(y):
            if 1<=d<=29:
                return True
            else:
                return False
        elif m==2 and not judge_yoon(y):
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
            if 1<=d<=30:
                return True
            else:
                return False
    elif 8<=m<=12:
        if m%2==0:
            if 1<=d<=31:
                return True
            else:
                return False
        else:
            if 1<=d<=30:
                return True
            else:
                return False
    else:
        return False

def find(m):
    if 3<=m<=5:
        return "Spring"
    elif 6<=m<=8:
        return "Summer"
    elif 9<=m<=11:
        return "Fall"
    elif m==12 or m>=1:
        return "Winter"

Y, M, D = map(int, input().split())
if judge(Y,M,D):
    print(find(M))
else:
    print(-1)