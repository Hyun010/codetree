l=[]
for _ in range(10):
    l.append(input())
c=input()
a=[]
for w in l:
    if w[-1]==c:
        a.append(w)
if a:
    for i in range(len(a)):
        print(a[i])
else:
    print("None")