class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return self.height * self.base / 2
    
    def change_size(self, b, h ):
        self.base = b
        self.height = h

Triangle1 = Triangle(10, 5)
print(Triangle1.area())