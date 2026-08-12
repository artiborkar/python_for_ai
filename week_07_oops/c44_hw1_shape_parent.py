# Homework
# Shape parent; Triangle aur Square children, dono ka apna area().

# 1=restate=Shape parent; Triangle aur Square children, dono ka apna area().
# 2=example= class Shape ,class Square(Shape):,class Triangle(Shape):
# 3=psuedocode=1.create 1st parent class shape with attribute self.name  and special method __init
#              2.create 1st child class square with parent class is shape attribute is num and method is area_square
#              3.create 2nd child class triangle with parent is shape attribute is height ,base method is area().AttributeError
#              4.there are two object square_obj = Square("Square",4) and triangle_obj = triagnle("Rectangle",4,5)
#              5.call the method square_obj.area() and triangle_obj.area().
# 4=translate=
# 5=dryrun=
# square_obj = Square("Square",4)
# class Shape :
    # def __init__(self,name:str)->str:
        # self.name = name
# square_obj.area_square()
# def area_square(self):
#         n=self.num*self.num
#         print(f"{self.name} area of {self.num} is {n}  ")
# triangle_obj = Rectangle("triangle",4,5)
# class Shape :
#     def __init__(self,name:str)->str:
#         self.name = name
# triangle_obj.area()
# def area(self):
#         result = self.heigth*self.base/2
#         print(f"{self.name} area is {result} ")

print("------------HOMEWORK 1---------------")

'''
create the class 1st parent class Shape:
    attribute 
        self.name :name of the shapes
    method:
         __init__:special method

2nd class for 1st child is square with parent animal:
    attribute:
        self.num:number of the square.
    method:
        area_square:calculate the square. 

3rd class for 2nd child is rectangle with parent animal:
    Attribute:  
        self.width:width of the rectangle
        self.length :length of the rectangle
    method:
        area_rectangle: claculate the area of rectangle.

'''


class Shape :
    def __init__(self,name):
        self.name = name



class Triangle(Shape):
    def __init__(self,name,height,base):
        super().__init__(name)
        self.height = height
        self.base = base
     
    def area(self):
        result = self.height*self.base/2
        print(f"{self.name} area is {result} ")

        

class Square(Shape):
    def __init__(self,name,num):
        super().__init__(name)
        self.num = num

    def area(self):
        n=self.num*self.num
        print(f"area of {self.name}is  {self.num} is {n}  ")




print("------------trangle----------")



triangle_obj = Triangle("trangle",5,6)
triangle_obj.area()


print("--------Square-----------")

square_obj = Square("Square",4)
square_obj.area()

print("-------polymorphisum--------")

shapes = [triangle_obj,square_obj]

for shape in shapes:
    shape.area()