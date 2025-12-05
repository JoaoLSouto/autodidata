class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_perimeter(self):
        return 4 * self.side_length

rectangle1 = Rectangle(4, 6)
print(rectangle1.calculate_perimeter()) 

square1 = Square(4)
print(square1.calculate_perimeter())