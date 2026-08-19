# 1. Composition + @property + _str_()

# Laptop class banao jo Battery object rakhe.

# Battery:

# capacity attribute ho.

# Laptop:

# Composition se Battery ka object rakho.
# @property se battery capacity access karo.
# Setter mein check karo ki capacity 1000 se kam na ho.
# _str_() se output do:

# Laptop Battery: 5000 mAh

'''
1=restate=Laptop class banao jo Battery object rakhe..
2=example=class Battery :,@property, @capacity.setter,class Laptop :
3.psudocode=1.Laptop class banao jo Battery object rakhe.
            2.Battery:capacity attribute ho.
            3.Laptop: Composition se Battery ka object rakho.
            4.@property se battery capacity access karo.
            5.Setter mein check karo ki capacity 1000 se kam na ho.
             6. _str_() se output do:

'''

# 4=translate=
from glob import translate


print("-------------p1------------------")

# class Battery :
#     def __init__(self,capacity):
#         self.capacity = capacity

#     @property
#     def capacity(self):
#         return self._capacity

#     @capacity.setter
#     def capacity(self,value):
#         if value < 1000 :
#             raise ValueError ("battery capacity can not be less than 1000 mAh")
#         self._capacity = value


# class Laptop :
#     def __init__(self,  capacity):
#         self.battery = Battery(capacity)

#     def __str__(self):
#         return f"Laptop Battery is {self.battery.capacity} mAh"

# laptop = Laptop(4000)

# print(laptop)

# laptop = Laptop(400)

# print(laptop)






print("-------------p-2--------------")


# 2. Inheritance + _str_()

# Person parent class banao:

# name attribute ho.
# _str() method "Name: __" return kare.

# Student class ko Person se inherit karo:

# marks attribute add karo.
# _str_() override karo.
# Output:

# Name: Asha, Marks: 85

'''
1=reatate= write the program to Inheritance + _str_()
2=example=class Person:,def __str__(self):,class Student(Person):
3=psuedocode=1.Person parent class banao:,name attribute ho.
             2._str() method "Name: __" return kare
             3. Student class ko Person se inherit karo,marks attribute add karo.
             4.__str__() override karo.
             5.s = Student("asha" , 85),print(s)
4=translate to python =


'''

# class Person:
#     def __init__(self,name):
#         self.name = name

#     def __str__(self):
#         return f"Name : {self.name.title()} "

# class Student(Person):

#     def __init__(self, name , marks):
#         super().__init__(name)
#         self.marks = marks

#     def __str__(self):
#         return f"Name : {self.name.title()} , Marks : {self.marks} "
    

# s = Student("asha" , 85)

# print(s)

# p = Person("arti")

# print(p)


# 5=dry run






print("---------------------p.3---------------------")

# 3. Encapsulation + _str_()

# BankAccount class banao:
# owner aur private __balance rakho.
# deposit(amount) method banao.
# get_balance() method se balance return karo.
# _str_() define karo.
# print(object) karne par:
# Owner: Asha, Balance: 5000 aaye.
 
'''
1=restate= write the code for Encapsulation + _str_()
2=example=class BankAccount:,def deposit(self,amount):,def get_balance(self):,def __str__(self):
3=psuedocode=1.BankAccount class banao:,owner aur private __balance rakho.
             2. deposit(amount) method banao.,self._balance += amount
             3.get_balance() method se balance return karo.,
4=translate to python
5=dry run 

'''

# class BankAccount:

#     def __init__(self,owner):
#         self.owner = owner.title()
#         self._balance = 0


#     def deposit(self,amount):
#         self._balance += amount


    
    
#     def get_balance(self):
#         return self._balance

#     def __str__(self):
#         return f" Owner : {self.owner} ,  Balance : {self._balance}"


# bankaccount = BankAccount("astha")

# bankaccount.deposit(1000)

# print(bankaccount)





print("-----------------p.4.-------------------")

# 4. Magic Method — _repr_()
# Book class banao:
# title aur price attributes rakho.
# _repr_() method define karo.
# repr() call karne par:
# Book(title='Python', price=500)
# jaisa output aaye.


'''
1=restate= write the _repr_()
2=example=class Book:,def __repr__(self):
3=psuedocode=1.Book class banao:,title aur price attributes rakho.
             2._repr_() method define karo.,return f"Book (title = '{self.title}' , price = {self.price})"
             3.book = Book("python",500),print(book)
4=translate to python =


'''

# class Book:
#     def __init__(self , title , price):
#         self.title = title.title()
#         self.price = price


#     def __repr__(self):
#         return f"Book (title = '{self.title}' , price = {self.price})"

# book = Book("python",500)

# print(book)

# book


# 5=dry run =





print("----------------p.5.------------------")

# 5. Magic Method — _str_()

# Student class banao:
# name aur marks attributes rakho.
# _str_() method define karo.
# print(student_object) karne par:
# Name: Asha, Marks: 85 aaye.
 














































# . Composition — Library

# Library class banao jo Book aur Author objects rakhe (composition).

# Book mein title aur price ho.
# Author mein name ho.
# Library ke andar Book aur Author ke objects create karo.
# Title, price aur author name print karo

class Book:
    def title(self):
        print("")