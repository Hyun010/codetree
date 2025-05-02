l=["apple","banana","grape","blueberry","orange"]
c=input()
a=[]
for w in l:
    if w[2]==c or w[3]==c:
        a.append(w)
if a:
    for i in range(len(a)):
        print(a[i])
    print(len(a))
else:
    print(0)