
class person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def sleep(self,h):
        return f'{self.name} sleeps {h} hours'


class student(person):
    def __init__ (self, name, age, id):
        self.id = id
        super().__init__(name,age)

p1 = ("Alim", '18') 
s1 = ('Ali', '18', '21B03')

# print (s1.id)
print (p1)