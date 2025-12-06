class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Square(Shape):
    square_list = []

    def __init__(self, side_length):
        self.side_length = side_length
        self.square_list.append(self)

    def calculate_perimeter(self):
        return 4 * self.side_length
    
    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")


a_square = Square(29)
print(Square.square_list)
another_square = Square(93)
print(Square.square_list)