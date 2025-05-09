class Person:
    def __init__(self,id="codetree",level=10):
        self.id=id
        self.level=level

user2_id, user2_level = input().split()
user2_level = int(user2_level)

person1=Person()
person2=Person(user2_id,user2_level)
print(f'user {person1.id} lv {person1.level}')
print(f'user {person2.id} lv {person2.level}')