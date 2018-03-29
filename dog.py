class Dog:
    """ This is the beginning of a class for the domestic dog """
    
    def __init__(self, name):
        """ another comment """
        self.name = name

    def add_weight(self, weight):
        self.weight = weight

    


c = Dog('Rag')
c.add_weight(15)
c.breed = ('Doge')
c.color = ('Beige with black underside')
c.age = ('2.5 years')

x = Dog('Gingo')
x.add_weight(42)
x.breed = ('Akita')
x.color = ('White with gray stripe')
x.age = ('5 years')
#Dog One
print("Name:")
print(c.name)
print("Weight:")
print(c.weight)
print("Breed:")
print(c.breed)
print("Color:")
print(c.color)
print("Age:")
print(c.age)
#Dog Two      
print("Name:")
print(x.name)
print("Weight:")
print(x.weight)
print("Breed:")
print(x.breed)
print("Color:")
print(x.color)
print("Age:")
print(x.age)


