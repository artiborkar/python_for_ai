# class Intro:
#     def __init__(self,name):
#         self.name = name

#     def intro(self):
#         print(f"hello {self.name}")

# name1 = Intro("Arti")

# print(name1)

# name1.intro()

# # name1.name



# print("------------p.1-------------------")

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age


# student = Student("Arti",21)
# print(student.name)
# print(student.age)


# print("-----------p.2--------------")

# class Car:
#     def __init__(self,brand,color) -> str:
#         self.brand = brand
#         self.color = color

#     def show_info(self):
#         print(f"brand:{self.brand}")
#         print(f"color:{self.color}")
        
# car_obj = Car("Toyota","Red")
# car_obj.show_info()

# print("==========p.3================")

# 1=resatate= create the simple inheritance program
# 2=Example= same as speck method.
# 3=pseudocode=1.create the parent class animal and method is speak.
             # 2.child class is dog with parent Dog(Animal) ,and same speak method.
            #  3.then the object is dog_obj=Dog()
            # 4.dog_obj.speak()     method
# 4=translate=
# 5=dry run =


'''
1st parent class is :
    Animal:
         method:speak any animal sound
child class is:
    Dog
        method :same speak ,print the dog brak

object:
         call the object any name then = call the class 
         dog_obj =Dog()
         call the method like 
         dog_obj=speak.
'''

# class Animal:
#     def speak(self):
#         print("animal speak")

# class Dog(Animal):
#     def speak(self):
#         print("dog brak.........")

    
# # animal_obj = Animal()

# dog_obj = Dog()

# dog_obj.speak()
# # animal_obj.speak()

# print("-------------p.4------------------")

# # 1=restate=create the BankAccount class and  method is deposite.
# # 2=example=class BankAcconunt, deposite()
# # 3=pseudocode=1.class is BankAccount .
#                 # 2.then Special method __init__ 2nd method is deposite.
#                 # 3.then object is bank_account_obj_1= BankAccount()
# # 4=translate=
# # 5=dry run =

# '''
# class is Bankaccount 
#     method :
#         ___init__=special method
#         deposite=deposite if the amount.
#     print:

# object :
# bank_amount_obj_1 = BankAccount("Arti",500)

# bank_amount_obj_1.deposite(500)

# '''
# class BankAccount():
#     def __init__(self,account_holder,balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposite(self,amount):
#         # result=amount+self.balance
#         self.balance=self.balance+amount
#         print(f"Total amount:{self.balance}")

# bank_amount_obj_1 = BankAccount("Arti",500)


# bank_amount_obj_1.deposite(500)


# print("===============P.5================")

# class Animal:
#     def __init__(self) :
#         pass
#     def sound(self):
#         print("animal sound")

# class Dog(Animal):
#     def sound(self):
#         print("bark")

# class Cat(Animal):
#     def sound(self):
#         print("meow")

# Dog().sound()

# Cat().sound()



# print("------------------------")

# # n=int(input("enter the number of star:"))

# # for i in range(1,n+1):
# #     for j in range (n-i):               #j loop space
# #         print(" ", end=" ")
# #     for k in range (i):                #k loop stars
# #         print("*",end=" ")
# #     print()


# # print("---------------------------")\

# # n=int(input("enter the number of star:"))
# # for i in range (1,n+1):
# #     for j in range(n-i):
# #         print(" ", end=" ")
# #     for k in range (2*i-1):
# #         if k==0 or k==2*i-2 or i==n:
# #             print("*",end=" ")
# #         else:
# #             print(" ",end="")
#     print()
        
# print("=================================")

# n=int(input("enter the number of star:"))
# for i in range (1,n+1):
#     for j in range(n-i):
#         print(" ", end=" ")
#     for k in range (2*i-1):
#         print("*",end=" ")
#     print()


# print("--------------------------")


# n=int(input("enter the number of star:"))
# for i in range (3,0,-1):
#     for j in range(i):
#         print("*",end=" ")

#     print()


# print("--------------------------")
# n=int(input("enter the number of star:"))
# for i in range (1,n):
#     for j in range(i):
#         print("*",end=" ")
#     print()





print("===============practice question===============")

#  1=resatate= create the simple inheritance program
# 2=Example= same as speck method.
# 3=pseudocode=1.create the parent class animal and method is speak.
             # 2.child class is dog with parent Dog(Animal) ,and same speak method.
            #  3.then the object is dog_obj=Dog()
            # 4.dog_obj.speak()     method



class Animal:
    def speak(self):
        print("Sound of any Animal")


class Dog(Animal):
    def speak(self):
        print("Dog brak Khuk khuk......")

Dog().speak()