from math import pi
class Figure:
    def __init__(self, color):
        self.color = color

class circle(Figure):
    def __init__(self,radius, color):
        self.radius = radius
        super().__init__(color)

    def get_area(self):
        return self.radius**2 * pi

    def get_length(self):
        return self.radius*2*pi

    def compare(self, p2):
        if self.get_area() > p2.get_area(): 
            return f'First one bigger'    
        else:
            return f'Second one is bigger'

class square(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_rec_area(self):
        return self.a * self.b
    def get_rec_per(self):
        return 2 * (self.a + self.b)

p1 = circle(5, 'green')
p2 = circle(10, 'yellow')
print(p1.get_area())
print(p1.compare(p2))