# 1. You should have at least four classes: the parent Animal class, and
# then at least three child animal classes that inherit from Animal.
# 2. Each class should have a few attributes and at least one method
# that models some behavior appropriate for a speciﬁc animal or all
# animals—such as walking, running, eating, sleeping, and so on.
# 3. Keep it simple. Utilize inheritance. Make sure you output details
# about the animals and their behaviors.



class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
      print(f"{self.name} is sleeping")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} is barking")

class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color = color

    def meow(self):
        print(f"{self.name} the {self.color} cat is meowing")

class Bird(Animal):
    def __init__(self,name,species):
        super().__init__(name)
        self.species = species

    def fly(self):
        print(f"{self.name} the {self.species} is flying")



my_dog = Dog("saka","german sherpard")
my_dog.eat()
my_dog.bark()

my_cat = Cat("trossard","green")
my_cat.sleep()
my_cat.meow()

my_bird = Bird("martinelli","parrot")
my_bird.eat()
my_bird.fly()