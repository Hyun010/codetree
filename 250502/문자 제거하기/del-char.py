s=list(input())
while len(s)>1:
    n=int(input())
    if n>=len(s):
        s.pop()
        print("".join(s))
    else:
        s.pop(n)
        print("".join(s))