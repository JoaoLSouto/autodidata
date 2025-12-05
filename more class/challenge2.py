class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_perimeter(self):
        return 4 * self.side_length
    
    def area(self):
        return self.side_length ** 2
    
    def change_size(self, side_length):
        self.side_length = side_length

square1 = Square(4)
print(square1.area())

square1.change_size(5)
print(square1.area())