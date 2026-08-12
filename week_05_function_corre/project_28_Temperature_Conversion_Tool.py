# Project 28 — Temperature Conversion Tool (multi-mode)
# EN: Write three functions: c_to_f(c), f_to_c(f), c_to_k(c). Run a while menu asking which conversion the user wants,
#  take the value, call the right function, and print the result. Loop until the user chooses Exit.
# हिंदी: तीन functions बनाओ: c_to_f(c), f_to_c(f), c_to_k(c)। एक while menu चलाओ जो पूछे कौन-सा conversion चाहिए, value लो, सही 
# function call करो, और result print करो। Exit चुनने तक loop चलाओ।
# Concepts: several functions, menu dispatch, float(input()), loop
# Hint: f_to_c = (f - 32) * 5 / 9; c_to_k = c + 273.15.




def c_to_f(c):
    return (c*9/5)+32

def f_to_c(f):
    return (f-32)*5/9

def c_to_k(c):
    return c+273.15

while True:

    print("\n--- Temperature Conversion Tool ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Exit")

    user = input("Enter any conversion :")

    if user ==  "1":
        c=float(input("Enter the Celsius : "))
        print(f"Fahrenheit is : {c_to_f(c):.2f} ")

    elif user == "2":
        f=float(input("Enter The Fahrenheit:"))
        print(f" Celsius is  : {f_to_c(f):.2f} ")

    elif user == "3":
        c=float(input("Enter the Celsius:"))
        print(f"Kelvin is : {c_to_k(c):.2f} ")

    elif user == "4":
        print("Exit")
        

    else :
        print("Invalied Temperature Conversion Tool ")
        
    break


