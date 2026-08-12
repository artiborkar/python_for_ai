# Ek Circle class with radius aur method area() jo area return kare



class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2

circle_obj = Circle(25)

print(circle_obj.area())

print(circle_obj.radius)