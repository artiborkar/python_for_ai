# Square class mein area property banao.


# 1=restate=Square class mein area property banao.
# 2=example=class Square:,@property
# 3=psuedocode=1.class Square method is def __init__(self,side),attribute is self.side=side
#               2.@property  ,method def area(self),return self.side*self.side
#               3.obect is s=Square(5)and print(s.aera())
# 4=translate=

print("-------homework 1------------")
class Square:

    def __init__(self,side):
        self.side=side

    
    @property
    def area(self):
        return self.side*self.side
    
s=Square(5)

print(s.area)

# 5=dry run =
# s=Square(5)
# def __init__(self,side):
        # self.side=side
# print(s.area)
# @property
#     def area(self):
#         return self.side*self.side
