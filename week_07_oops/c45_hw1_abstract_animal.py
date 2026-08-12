# Ek abstract Animal banao with abstract sound(). Dog aur Cat se implement karo.

# 1=restate =Ek abstract Animal banao with abstract sound(). Dog aur Cat se implement karo.
# 2=example=class Animal(ABC):,class Dog(Animal):,class Cat(Animal):
# 3=pseudocode =1. from abc import ABC , abstractmethod
              # 2.class Animal(ABC): with method sound
              # 3.class Dog (Animal)with methid sound.
              # 4.print the sound of the animal   
# 4=translate=
# 5=dry run =
# print(Cat().sound())
# from abc import ABC , abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         ...
# class Cat(Animal):
#     def sound(self):
#         return "meow meow......."

# print(Dog().sound())
#  from abc import ABC , abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         ...
# class Dog(Animal):

#     def sound(self):
#         return "khuk khuk ........."



print("-----------HOMEWORK-----------")


'''
from abc import ABC , abstractmethod
create the class parent ABC
    class Animal chlid parent ABC.
method:
    sound()--sound of any animal

create 2 child class dog and cat with parent class.
    class Dog(Animal)
    class Cat(Animal)
method :
    sound ---sound of cat and dog animal

print the sound of the animal.

'''

from abc import ABC , abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        ...

class Dog(Animal):

    def sound(self):
        return "khuk khuk ........."

class Cat(Animal):
    def sound(self):
        return "meow meow......."

print(Cat().sound())

print(Dog().sound())