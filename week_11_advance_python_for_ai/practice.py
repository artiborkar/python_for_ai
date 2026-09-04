# Ek @greet decorator banao jo function call hone se pehle print kare: Hello! Function is starting...



print("------------1---------------") 

def greet(func):
    def wrapper():
        print("Hello! Function is starting...")
        result = func()
        return result
    return wrapper

@greet

def greeting():
    return "Hello Artiiiiiiiiiiiii !"

print(greeting())





print("-------------2. Goodbye Decorator---------------")


# 2. Goodbye Decorator
# Ek @bye decorator banao jo function execute hone ke baad print kare:
# Goodbye! Function finished.


def bye(func):
    def wrapper():
        result = func()
        
        print("Goodbye! Function finished.")
        return result
    return wrapper

@bye
def goodbye():
    return "Byeeee !"

print(goodbye())






print("-------------  3. Count Calls---------------")

# 3. Count Calls
# Ek @count_calls decorator banao jo bataye function kitni baar call hua.
# Expected:
# Function called 1 times
# Function called 2 times
# Function called 3 times




def count_calls(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        result  = func()
        print(f"Function called {count} times")
        return result

    return wrapper

@count_calls

def count():
    ''' return "Doneeee" '''
    pass

count()

count()

count()

''' print(count())

 print(count())

print(count()) '''




print("------------- 4. Timer Decorator ⭐----------------")



# 4. Timer Decorator ⭐
# Ek @timer decorator banao jo function ko execute hone mein kitna time laga, wo print kare.
# Function ke andar loop use karo:


import re
import time
from unittest import result


def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"You time takes {end - start} seconds")
        return result
    return wrapper

@timer 
def timing():
    for i in range(1000000):
        pass


timing()





print("------------- 5. Uppercase Decorator----------------")


# Level 2 — Thoda Practice

# 5. Uppercase Decorator
# Ek @uppercase decorator banao jo function ke returned string ko uppercase mein convert kare.

def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase
def upper_case():
    return "my name is arti borkar"


print(upper_case())





print("------------- 6. Double Result----------------")


# 6. Double Result
# Ek @double decorator banao jo function ke returned number ko 2 se multiply kare.


def double(func):
    def wrapper(*args):
        result = func(*args)
        return result *2

    return wrapper

@double
def mult(x,y):
    return x*y

print(mult(3,3))





print("-----------------7. Before & After------------------------")


# 7. Before & After
# Ek decorator banao jo function se pehle aur baad mein message print kare:
# Function Started
# Hello Python
# Function Ended

def my_decorator(func):
    def wrapper():
        print("The Function Start")
        result = func()
        
        print(result)
        print("The Function Ended")
        
        
    return wrapper
    

@my_decorator
def new():
   return "Hello Python"
   

new()







print("-----------------8. Check Positive Number------------------------")

# 8. Check Positive Number
# Ek @check_positive decorator banao jo function ke result ko check kare.
# Agar result positive hai:
# Positive number
# Otherwise:
# Negative number


def check_positive(func):
    def wrapper(a):
        result = func(a)
        if a > 0:
            print("Positive Number")

        else :
            print("Negative Number")



    return wrapper

@check_positive

def pos_neg(a):
    return a

pos_neg(4)

pos_neg(-4)








print("----------------- 9. Login Decorator ⭐------------------------")

# Level 3 — Challenge
# 9. Login Decorator ⭐
# Ek @login_required decorator banao.
# is_logged_in = True
# Agar True hai:
# Welcome to Dashboard
# Agar False hai:
# Please login first

def login_required(func):
    def wrapper(a):
        result = func(a)
        if result == True:
            print("Welcome to Dashboard")

        else:
            print("Please login first")
        

    return wrapper

@login_required
def is_logged_in(a):
    return a


is_logged_in(1)

is_logged_in(0)

is_logged_in(True)

is_logged_in(False)







print("----------------- 10. Repeat Decorator ------------------------")

# 10. Repeat Decorator 🔥
# Ek @repeat(3) decorator banao jo function ko 3 times execute kare.

# @repeat(3)
# def hello():
#     print("Hello")
# Output:
# Hello
# Hello
# Hello

def repeat(n):
    def repeat_fun(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return repeat_fun

@repeat(3)
def hello():
    print("Hello")

print(hello())
# hello()
# hello()