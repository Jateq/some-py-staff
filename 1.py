class person:
    def __init__ (self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def info(self):
        return f'{self.name} is {self.age} years old'
P1 = person('Dias', 18, 'Male')

print(P1.name, P1.age, P1.gender, P1.info)
# pass is for empty method

class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width 
    def get_area(self):
        return self.length * self.width

r1 = rectangle(3, 6)
r2 = rectangle(5, 10)
print(r1.get_area)