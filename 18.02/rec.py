class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width 

    def get_area(self):
        return self.length * self.width
    def compare(self, r2):
        pass
r1 = rectangle(3, 6)
r2 = rectangle(5, 10)
print(r1.get_area)