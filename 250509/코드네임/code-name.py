class Person:
    def __init__(self,codename,score):
        self.codename=codename
        self.score=score
        
MAX_N = 5
codenames = []
scores = []
persons=[]
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))
for c,s in zip(codenames,scores):
    persons.append(Person(c,s))
persons.sort(lambda x: x.score)
print(persons[0].codename,persons[0].score)