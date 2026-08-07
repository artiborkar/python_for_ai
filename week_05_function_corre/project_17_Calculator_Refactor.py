# Project 17 — Calculator Refactor (many small functions)
# EN: Refactor a calculator into functions: add, subtract, multiply, divide (handle divide-by-zero by returning a message). Then write calculate(a, b, op) that calls the right one based on op ("+", "-", "*", "/").
# हिंदी: Calculator को functions में बाँटो: add, subtract, multiply, divide (divide-by-zero पर message return करो)। फिर calculate(a, b, op) बनाओ जो op ("+", "-", "*", "/") के हिसाब से सही function call करे।
# Concepts: many functions, dispatch with if/elif or match, return
# Hint: In divide, if b == 0: return "Cannot divide by zero".



print("=====Calculator Refactor =========")

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

x=int(input("Enter the First Number:"))
y=int(input("Enter the Second Number:"))

user=input("Enter the any oprator are perfrom (+,-,*,/):")

if user == "+":
    print(f"Addition of two Number : {add(x,y)}")

elif user == "-":
    print(f"Substract of two Number : {sub(x,y)}")

elif user == "*":
    print(f"Multification of two Number : {mul(x,y)}")

elif user == "/":
    print(f"Divistion of two Number : {div(x,y)}")

else:
    print("invalied opretor")
