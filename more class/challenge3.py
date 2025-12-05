class Shape:
    def what_am_i(self):
        print("I am a shape")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_perimeter(self):
        return 4 * self.side_length


rectangle1 = Rectangle(4, 6)
print(rectangle1.calculate_perimeter())
rectangle1.what_am_i()

square1 = Square(4)
print(square1.calculate_perimeter())
square1.what_am_i()
