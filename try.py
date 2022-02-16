s = 'coffee'
n = 5
result1 = f'저는 {s}를 좋아합니다. 하루 {n}잔 마셔요.'



class Pet():
    #__tablename__ = 'pets' # table inside of pets.db is 'pets'

    id = '아이디'
    name = '이름'
    age = '나이'
    pet_type = 'type'

    def __repr__(self):
        return f'{self.id} | {self.name} {self.age} {self.pet_type}'

print(Pet().id)