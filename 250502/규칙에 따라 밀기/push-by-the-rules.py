s=input()
q=list(input())
for i in q:
    if i=="L":
        s=s[1:]+s[0]
    elif i=="R":
        s=s[len(s)-1]+s[:len(s)-1]
print(s)