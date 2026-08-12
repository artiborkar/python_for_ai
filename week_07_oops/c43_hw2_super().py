# Shape parent (with name); Square aur Rectangle children with super().

# 1=restate=classes are three shape is parent class and square and rectagle is chile class.
# 2=example= class Shape ,class Square(Shape):,class Rectangle(Shape):
# 3=psuedocode=1.create 1st parent class shape with attribute self.name  and special method __init
#              2.create 1st child class square with parent class is shape attribute is num and method is area_square
#              3.create 2nd child class rectangle with parent is shape attribute is width ,length method is area_rectagle.AttributeError
#              4.there are two object square_obj = Square("Square",4) and rectangle_obj = Rectangle("Rectangle",4,5)
#              5.call the method square_obj.area_square() and rectangle_obj.area_rectangle().
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
# rectangle_obj = Rectangle("Rectangle",4,5)
# class Shape :
#     def __init__(self,name:str)->str:
#         self.name = name
# rectangle_obj.area_rectangle()
# def area_rectangle(self):
#         result = self.width*self.length
#         print(f"{self.name} area is {result} ")



print("--------------HOMEWORK 2---------------")

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
    def __init__(self,name:str)->str:
        self.name = name


        

class Square(Shape):
    def __init__(self,name,num:int)->int:
        super().__init__(name)
        self.num = num



    def area_square(self):
        n=self.num*self.num
        print(f"{self.name} area of {self.num} is {n}  ")



class Rectangle(Shape):
    def __init__(self,name,width:int,length:int)->int:
        super().__init__(name)
        self.width = width
        self.length = length
     
    def area_rectangle(self):
        result = self.width*self.length
        print(f"{self.name} area is {result} ")


print("--------Square-----------")

square_obj = Square("Square",4)
square_obj.area_square()

print("------------rectangle----------")

rectangle_obj = Rectangle("Rectangle",4,5)
rectangle_obj.area_rectangle()