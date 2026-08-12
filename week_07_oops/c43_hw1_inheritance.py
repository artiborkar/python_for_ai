# Homework
# Animal parent banao; Cat aur Cow children banao, har ek apni awaaz wala method.


# 1=restate=craete the class parent or child parent clas is animal or child class is cat or cow.
# 2=example= class Animal ,class Cat or class cow
# 3=psuedocode=1.create the 1st class is parent class is Animal .
#              2.create the special method and __init__ or paprameter is(self ,name)
#              3. attribute is self.name.
#              4. 2nd method is eat not parameter is pass but by default parameter is self and print
#              5.1 child class is cat and provide the parent class(Animal)
#              6.method is cat_tone(->str) and print
#              7.2 nd child is cow and provide the parent(Animal)
#              8.method is cow_tone(str) and print
#              9.create 2 object like cat_obj and cow_obj
#              10.and cat_obj.cat_tone() and cow_obj.cow_tone
# 4=translate=
# 5=dry run=
# cat_obj=Cat("mini")
# class Animal:
#     def __init__(self,name:str)->str:
#         self.name = name

# cat_obj.cat_tone()
# class Cat(Animal):
#     def cat_tone(self)->str:
#         print(f"{self.name} says Meow meow")

# cat_obj.eat()
#  def eat(self):
#         print(f"{self.name} is eating")



print("-------HOMEWORK 1------------")


'''
class is to represent a Animal as a parent or base class.
    Attribute:
        name ( str): the name of the animal.
    method
        __init__:is a constractor or special method of the class.
        eat->str:animal is eating 

second class of cat is the child of the animal class
    method :
        cat_tone ->str: cat says meow meow

third class of  cow is the child of animal class:
    method:
        cow_tone->str: cow says moo

'''

class Animal:
    def __init__(self,name:str)->str:
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")


class Cat(Animal):
    def cat_tone(self)->str:
        print(f"{self.name} says Meow meow")


class Cow(Animal):
    def cow_tone(self)->str:
        print(f"{self.name} says Moo")



print("-------cat-------")

cat_obj=Cat("mini")

cat_obj.cat_tone()
cat_obj.eat()

print("-------cow-------")

cow_obj = Cow("pushpa")

cow_obj.cow_tone()
cow_obj.eat()



