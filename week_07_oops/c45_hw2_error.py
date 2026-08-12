# Jaan-boojh kar ek child banao jo sound() na likhe — error padho.

# print("--------HOMEWORK------------")

from abc import ABC , abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        ...

class Dog(Animal):

    def area(self):
        return "khuk khuk ........."

print(Dog().sound())


# TypeError: Can't instantiate abstract class Dog without an implementation for abstract method 'sound'