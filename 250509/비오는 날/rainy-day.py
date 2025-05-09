class T:
    def __init__(self,date,day,weather):
        self.date=date
        self.day=day
        self.weather=weather

n = int(input())
date = []
day = []
weather = []
for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)
l=[]
for t,y,w in zip(date,day,weather):
    l.append(T(t,y,w))
l.sort(lambda x: x.date)
for i in l:
    if i.weather=="Rain":
        print(i.date, i.day, i.weather)
        break