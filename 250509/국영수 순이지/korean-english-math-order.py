class P:
    def __init__(self,name,k,e,m):
        self.name=name
        self.korean=k
        self.english=e
        self.math=m

n = int(input())
name = []
korean = []
english = []
math = []
for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))
l=[]
for n,k,e,m in zip(name,korean,english,math):
    l.append(P(n,k,e,m))
l.sort(key=lambda x: (-x.korean,-x.english,-x.math))
for k in l:
    print(k.name, k.korean, k.english, k.math)