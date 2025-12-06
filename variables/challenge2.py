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

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side_length, self.side_length, self.side_length, self.side_length)    

a_square = Square(29)
print(a_square)

another_square = Square(93)
print(another_square)    