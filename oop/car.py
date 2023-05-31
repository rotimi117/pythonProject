class Car:
    def __init__(self,color, mileage):
        self.color = color
        self.mileage = mileage

    def __drive__(self,miles):
        self.mileage += miles


blue_car = Car("blue",20000)
red_car = Car("red",30000)

print(f"the {blue_car.color} car has {blue_car.mileage} miles ")
print(f"The {red_car.color} car has {red_car.mileage} miles")

my_car = Car("blue" ,0)
print(f"Initial mileage: {my_car.mileage}")
my_car.__drive__(100)
print(f"New mileage after driving 100 miles: {my_car.mileage}")