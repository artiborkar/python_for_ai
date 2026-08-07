# Project 3 — Simple Interest Calculator
# EN: Write a function simple_interest(principal, rate, years) that returns the simple interest (P × R × T) / 100. Print interest for ₹10000 at 5% for 3 years.
# हिंदी: एक function simple_interest(principal, rate, years) बनाओ जो simple interest (P × R × T) / 100 return करे। ₹10000 पर 5% की दर से 3 साल का interest print करो।
# Concepts: three parameters, return
# Hint: return (principal * rate * years) / 100.

'''
restate=calculte simple intrest calculator
example=(principal * rate * years) / 100. this is given 
psuedocode = 1 create function with function name is simple_interest is given 
             2 then return the formulas (principal * rate * years) / 100.
             3 print the function name and agruments
translate=
dry run =
 def simple_interest(principal, rate, years)
 (1000,5,3)
 return (principal * rate * years) / 100
print(simple_interest(1000,5,3))
150
'''

print("========Simple Interest Calculator==========")

def simple_interest(principal, rate, years):
    return (principal * rate * years) / 100

print(simple_interest(1000,5,3))