# Apne my_tools.py(week 5)ke 3 function mein type hints + google-style doctstring add karo.

# function one 1.

def add(num1:int,num2:int)->int:
    '''
    parameter
        num1:number 1 is intinger
        num2: number 2 is intinger

    claculate the sum
        num1+num2
        our output is intinger
    return 
    '''

    return num1 + num2

print(add(4,6))

print(add.__doc__)

print("-----------------------------------")

# function 2

def greet(x:str)->str:
    '''
    just print hello+name
    parameter is 
        x
    return 
        hello {x}
    '''

    return f"Hello {x}"

print(greet("Artiii"))

print(greet.__doc__)


print("-----------------------------------")


def fact(m:int)->int:
    '''
    calculate the factorial number:
        parameter is m
    if 
        m == 1 
        return 1
    return 
        m*fact(m-1)

    print(fact(m))

    '''
    if m == 1:
        return 1
    return m* fact(m-1)
print(fact(5))

print(fact.__doc__)

print("-----------------------------------")