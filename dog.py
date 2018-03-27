class Dog:
    """ This is the beginning of a class for the domestic dog """
    
    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight


c = Dog('Rag')
# c.name = "Fluffy"

x = Dog('Gingo')
# x.name = "Spike"

x.add_weight(42)
# x.add_wieght(12)

print(c.name)

print(x.name)
print(x.weight)
