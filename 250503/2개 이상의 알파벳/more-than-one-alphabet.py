def check(s):
    s=list(s)
    t=s[0]
    for i in range(1,len(s)):
        if t!=s[i]:
            return True
    return False

A = input()
if check(A):
    print("Yes")
else:
    print("No")