def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


# -----------------------------------------
import math

def is_palindrome(text: str) -> bool :
    '''
    function:
        is_palindrome:
            parameter: is text and return in str or
            output : is bool value

    return :


    '''

    if text==text[::-1]:
        return True
    else:
        return False


# ---------------------------------------------

def circle_area(radius) :
    '''
        return :
                circle area
        formula:
                pi(3.14)*radius**2
    '''
    return math.pi * radius ** 2
    #pi==3.14


# -------------------------------------------

def greating(name:str)-> :
    print(f"Hello  {name}")