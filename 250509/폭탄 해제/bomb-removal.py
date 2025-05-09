class T:
    def __init__(self,code,color,second):
        self.code=code
        self.color=color
        self.second=second

unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)
t=T(unlock_code,wire_color,seconds)
print(f'code : {t.code}')
print(f'color : {t.color}')
print(f'second : {t.second}')