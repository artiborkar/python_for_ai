# Project 2 — Temperature Converter
# EN: Write a function celsius_to_f(c) that converts Celsius to Fahrenheit and returns the value. Test it with 0, 37, and 100 degrees.
# हिंदी: एक function celsius_to_f(c) बनाओ जो Celsius को Fahrenheit में बदल कर value return करे। इसे 0, 37 और 100 डिग्री पर test करो।
# Concepts: def, arithmetic, return
# Hint: Formula: (c * 9 / 5) + 32.


'''
step 1=restate=calculate the fahrenheit (c * 9 / 5) + 32 give.
step 2=example =(c * 9 / 5) + 32 this is given and print 
step 2=pseudocode=1 create the function and funaction name is celsius_to_f
                  2 parameter is c
                  3 retun the formulas like (c * 9 / 5) + 32 
                  4 print the function name and argument

step 4 translate=
step 5 Dry run= 
celsius_to_f(c)
celsius_to_f(34)
return (c * 9 / 5) + 32
print(celsius_to_f(34))
93.2

'''

print("====Project 2 — Temperature Converter=====")

def celsius_to_f(c):

    return (c * 9 / 5) + 32

print(celsius_to_f(34))