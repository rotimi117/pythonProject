class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length,side_length)


my_rectangle = Rectangle(6,2)
print(f"Rectangle area: {my_rectangle.area()}")

my_square = Square(6)
print(f"Square area: {my_square.area()}")

