class Dog:
    """ This is the beginning of a class for the pet Dog"""
    
    def __init__(self, name):
        """ another comment """
        self.name = name

class Snake:
    """ This is the beginning of a class for the pet Snake"""
    
    def __init__(self, name):
        """ another comment """
        self.name = name


class Otter:
    """ This is the beginning of a class for the pet Otter"""
    
    def __init__(self, name):
        """ another comment """
        self.name = name

#Dog class
d = Dog('Lokey')
d.breed = ('American Bulldog')
d.color = ('Brown with Orange spots')
d.age = ('16 months')
d.sound = ('ork ork')
d.temperment = ('Unyeiling')
#snake class
s = Snake('Ghost')
s.breed = ('Ball Python')
s.color = ('Albino')
s.age = ('18 weeks')
s.sound = ('Ssss')
s.temperment = ('Agitated')
#otter class
o = Otter('Repu')
o.breed = ('Asian Small Claw')
o.color = ('Grey')
o.age = ('2 years')
o.sound = ('Squeak')
o.temperment = ('calm')
#printing dog
print("Pet:")
print(d.name)
print("Breed:")
print(d.breed)
print("Age")
print(d.age)
print("Sound:")
print(d.sound)
print("Temperment:")
print(d.temperment)
print("___________")
#printing snake
print("Pet:")
print(s.name)
print("Breed:")
print(s.breed)
print("Age")
print(s.age)
print("Sound:")
print(s.sound)
print("Temperment:")
print(s.temperment)
print("___________")
#printing otter
print("Pet:")
print(o.name)
print("Breed:")
print(o.breed)
print("Age")
print(o.age)
print("Sound:")
print(o.sound)
print("Temperment:")
print(o.temperment)
print("___________")
