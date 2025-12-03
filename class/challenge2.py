import math

class Circle:
    def __init__(self, r, p):
        self.r = r
        self.pi = p

    def area(self):
        return self.r ** 2 * math.pi

    def change_size(self, r, p):
        self.r = r
        self.pi = p

circle1 = Circle(5, 3.14)
print(circle1.area())

circle1.change_size(10, 3.14)
print(circle1.area())