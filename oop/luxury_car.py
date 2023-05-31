class Car:
    def __init__(self,model,year):
        self._model = model
        self._year = year
        self._speed = 0

    def model(self):
        return self._model

    def year(self):
        return self._year

    def speed(self):
        return self._speed

    def acceleration(self,faster):
        self._speed += faster

    def deacceleration(self,slower):
        if self._speed >= slower:
            self._speed -= slower
        else:
            self._speed = 0



my_car = Car("range rover", 2023)
print(f"model :{my_car.model()}")
print(f"year : {my_car.year()}")
print(f"speed : {my_car.speed()}")

my_car.acceleration(120)
print(f"Speed after accelerating: {my_car.speed}")

my_car.deacceleration(50)
print(f"Speed after deaccelerating: {my_car.speed}")

my_car.deacceleration(100)
print(f"Speed after attempting to decelerate: {my_car.speed}")



