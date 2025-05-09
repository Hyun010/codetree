class Con:
    def __init__(self,sc,mp,t):
        self.secret_code=sc
        self.meeting_point=mp
        self.time=t

secret_code, meeting_point, time = input().split()
time = int(time)
c=Con(secret_code,meeting_point,time)
print(f'secret code : {c.secret_code}')
print(f'meeting point : {c.meeting_point}')
print(f'time : {c.time}')