s=input()
for _ in range(len(s)+1):
    print(s)
    s=s[len(s)-1]+s[:len(s)-1]