class Rider:
    def __init__(self, name):
        self.name = name

class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

theyrider1 = Rider("Alice")
strongerhorse1 = Horse("Thunder", theyrider1)
print(strongerhorse1.rider.name)

print("The name of Horse is {}".format(strongerhorse1.name))
print("The name of Rider is {}".format(strongerhorse1.rider.name))        