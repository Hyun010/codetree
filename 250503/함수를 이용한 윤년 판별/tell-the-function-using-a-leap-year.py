def judge(n):
    if n%4==0:
        if n%100==0 and n%400!=0:
            return "false"
        else:
            return "true"
    else:
        return "false"

y = int(input())
print(judge(y))