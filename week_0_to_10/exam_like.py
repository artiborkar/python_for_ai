
'''
print("Week 0 – Python Basics")
print("-----------------Week 0 -1----------------------")
# 1.Write a Python program to take the user's name as input and print a greeting message.

name  = input("Enter the name :").title()

print(f"Hello , {name} !")



print("-----------------Week 0 -2----------------------")

#2.  Write a Python program to take two numbers as input and print their sum.

num1 = int(input("Enter the First Number:"))
num2 = int(input("Enter the Second Number:"))

print(f"sum of two Number : {num1 + num2 }")


print("-----------------Week 0 -3----------------------")

# 3.Write a Python program to convert Celsius temperature to Fahrenheit.

cel  =  float(input("Enter the Celsius temperature:"))

f = (cel * 9/5 ) + 32

print(f"Celsius temperature to Fahrenheit is : {f}")


print("-----------------Week 0 -4----------------------")

#4. Write a Python program to calculate the area of a circle.

# area of a circle. = π (pi) * r*r

radius = int(input("Enter the radius : "))

a = 3.14 * radius * radius 


print(f"Area of a Circle s : {a}")


print("-----------------Week 0 -5----------------------")

# 5. Write a Python program to take the user's age as input and display it.

age = int(input("Enter the Age : "))

print(age)

'''






'''

print("Week 1 – Data Types and Operators")

print("-----------------Week 1 -1----------------------")
#1. Write a Python program to perform addition, subtraction, multiplication, and division of two numbers.

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print(f"Addition of two Number is : {add(5,5)}")

print(f"substraction of two Number is  : {sub(5,5)}")

print(f"Multification of two Number is  : {mul(5,5)}")

print(f"Division of two Number is  : {div(5,5)}")




print("-----------------Week 1 -2----------------------")


# 2 . Write a Python program to check the data type of a user input.

var  = "Arti"
var1 = 34
var2 = 234.4
var3  = True
print(type(var))
print(type(var1))
print(type(var2))
print(type(var3))


print("-----------------Week 1 -3----------------------")

#3. Write a Python program to swap two variables.


a , b = 3 , 7

a , b = b ,a

print(a)
print(b)


print("-----------------Week 1 -4----------------------")

# 4.Write a Python program to concatenate two strings.

name = "Arti" 
lastname = "Borkar"

print(f"{name + lastname}")




print("-----------------Week 1 -5----------------------")

# 5. Write a Python program to check whether a number is even or odd.

num = int(input("Enter the Nunber : "))

if num % 2 == 0:
    print(f"{num} is Even")

else:
    print(f"{num} is Odd")

'''


'''


print("Week 2 – Conditions and Loops")

print("-----------Week 2 - 1-------------------")
# 1.Write a Python program to print numbers from 1 to 10 using a loop.

for num in range(1,11):
    print(num) 
    


    
print("-----------Week 2 - 2-------------------")

# Write a Python program to print all even numbers from 1 to 20.

for i in range(1,20):
    if i % 2 == 0:
        print(i)



print("-----------Week 2 - 3-------------------")

# Write a Python program to check whether a number is positive, negative, or zero.

num = int(input("Enter The Number : "))

if num > 0 :
    print("Positive")

elif num < 0 :
    print("Negative")

else :
    print("Zeroo")



print("-----------Week 2 - 4-------------------")

#4. Write a Python program to calculate the sum of numbers from 1 to n.


# Write a Python program to print the multiplication table of a given number.


'''
# Week 3 – Lists, Tuples and Strings
# Write a Python program to add an element to a list.
# Write a Python program to remove an element from a list.
# Write a Python program to find the largest number in a list.
# Write a Python program to reverse a string.
# Write a Python program to print all odd numbers from a list.
# Week 4 – Dictionary, Set and Comprehension
# Write a Python program to create a dictionary containing a student's name and marks.
# Write a Python program to access a dictionary value using the get() method.
# Write a Python program to add a new key-value pair to a dictionary.
# Write a Python program to create a list of squares from 1 to 10 using list comprehension.
# Write a Python program to remove duplicate values from a list using a set.
# Week 5 – Functions
# Write a function to calculate the sum of two numbers.
# Write a function using a default parameter.
# Write a function that returns the square of a number.
# Write a function using *args to calculate the sum of multiple numbers.
# Write a function using **kwargs to display student information.
# Week 6 – Lambda, Map, Filter and Modules
# Write a lambda function to add two numbers.
# Write a program using map() to double all numbers in a list.
# Write a program using filter() to find all even numbers from a list.
# Write a program using map() and a lambda function to find the square of each number.
# Create and import a custom Python module.
# Week 7 – Object-Oriented Programming
# Create a Student class with name and age attributes.
# Create a Car class with brand and model attributes.
# Create a BankAccount class with deposit and withdrawal methods.
# Write a program to demonstrate inheritance using Animal and Dog classes.
# Write a program to demonstrate polymorphism using Animal, Dog, and Cat classes.
# Week 8 – File and Exception Handling
# Write a Python program to write text into a file.
# Write a Python program to read the contents of a file.
# Write a Python program to handle division by zero using try-except.
# Write a Python program to safely read a file using exception handling.
# Write a Python program to count the number of lines in a text file.
# Week 9 – JSON, CSV and Logging
# Write a Python program to save student data into a JSON file.
# Write a Python program to load student data from a JSON file.
# Write a Python program to create a CSV file containing student names and marks.
# Write a Python program to read a CSV file using DictReader.
# Write a Python program to display info, warning, and error messages using logging.




print("Week 10 – Generators, Iterators and Decorators")

print("--------------Week 10 - 1---------------")

# Write a generator function countdown(n) that yields numbers from n to 1.

import sys

def my_func(n):
    for i in range(n , 0 , -1):

        yield i

g = my_func(5)

for num in g:
    print(num)






print("--------------Week 10 - 2---------------")



print("--------------Week 10 - 3---------------")
# Write a generator function that yields the square of numbers from 1 to n.

print("--------------Week 10 - 4---------------")
# Write a generator to print a sentence word by word.

print("--------------Week 10 - 5---------------")
# Write a simple Python decorator that displays a message before and after a function call.

# Total: 55 Practical Questions (5 questions × 11 weeks)