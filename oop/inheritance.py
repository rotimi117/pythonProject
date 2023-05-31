class Animal:

    # def __init__(self, age):
    #     self.age = age

    def __init__(self):
        self.age = 11

    def eat(self):
        print("Eating...")



class Mammal(Animal):

    def __init__(self):
        super().__init__()
        self.weight = 12
    def walk(self):
        print("walking...")

class Pisces(Mammal):

    def swim(self):
        print("swimming...")





m = Mammal()
m.eat()
f = Pisces()
print(m.age)
f.eat()
print(isinstance(Mammal, object))


