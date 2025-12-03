class Hexagon:
    def __init__(self, s):
        self.side_length = s

    def perimeter(self):
        return self.side_length * 6
    
    def change_size(self, s):
        self.side_length = s

Hexagon1 = Hexagon(4)
print(Hexagon1.perimeter())

