import math
# class Human:
#
#     def greet(self):
#         print("hello torin")
#
# Esther = Human()
# print(Esther.greet())

# class Human:
#     def __init__(self, name):
#         self.name = name
#     def greet(self):
#         print(f"hello {self.name}")
#
#     def walk(self):
#             print(f"{self.name} is walking")
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# human1 = Human("rotimi nicol")
# human2 = Human("bukayo saka")
# # human3 = Human("martin odeguard")
# # human1.greet()
# # human1.walk ()
# # human2.greet()
# # human3.greet()
# print(human1)

# class Circle:
#     def area(self, radius):
#         return 3.142 * (radius * radius)
#
#     def perimeter_of_a_circle(self, radius):
#         return 2 * 3.142 * radius
#
# circle = Circle()
# print(circle.area(4))
# print(circle.perimeter_of_a_circle(4))

class Circle:
    def area(self,radius):
        return math.pi * pow(radius , 2)

    def perimeter(self, radius):
        return 2 * math.pi * radius

circle = Circle()
print(f"the area is {circle.area(7):,.2f}")
print(f"the perimeter is {circle.perimeter(5):,.2f}")
