class Apple:
    def __init__(self, origin, color, weight, variety):
        self.origin = origin
        self.color = color
        self.weight = weight
        self.variety = variety

Apple1 = Apple("USA", "Red", 150, "Fuji")
print(Apple1)
print(Apple1.origin)
print(Apple1.color)
print(Apple1.weight)
print(Apple1.variety)