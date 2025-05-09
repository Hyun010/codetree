class P:
    def __init__(self,name,s1,s2,s3):
        self.name=name
        self.score1=s1
        self.score2=s2
        self.score3=s3

n = int(input())
name = []
score1 = []
score2 = []
score3 = []
for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))
l=[]
for m,s1,s2,s3 in zip(name,score1,score2,score3):
    l.append(P(m,s1,s2,s3))
l.sort(key=lambda x: x.score1+x.score2+x.score3)
for k in l:
    print(k.name, k.score1, k.score2, k.score3)