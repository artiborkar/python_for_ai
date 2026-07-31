# step 1 = restate = create a simple calculator or opretor is +,-,*,/,%,**,//
# step 2 = example = num1+num2,2+3=5,3-2=1 etc
# step 3 psuedocode =        1. create a function for every opretaors.
                            #2. then chech the condtion like .if user == + print sum
                            # 3. all same check in all condition like -,*,/,//,%,**
                            # 4. last then else print invaild opretor.
                            # 5. print output.

# step 4 translate python code:

4


def add(num1,num2):
    return num1+num2  

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

def modu(num1,num2):
    return num1%num2

def power(num1,num2):
    return num1**num2

def flo(num1,num2):
    return num1//num2

while True :

    print("============Well Come to calculator=============")

    num1 = int(input("Enter The first Number:"))
    num2 = int(input("Enter The second Number:"))
    user=input("Enter Any One operator like +,-,*,/,%,**,//:")

    if user == "+":
        print(f"Addition Of Two Number is: {add(num1,num2)}")

    elif user == "-":
        print(f"substraction Of Two Number  is: {sub(num1,num2)}")

    elif user == "*":
        print(f"Multification Of Two Number is: {mul(num1,num2)}")

    elif user == "/":
        print(f"Division Of Two Number is: {div(num1,num2)}")

    elif user == "%":
        print(f"Module Of Two Number is: {modu(num1,num2)}")

    elif user == "**":
        print(f"Power Of Two Number is: {power(num1,num2)}")

    elif user == "//":
        print(f"Floor Of Two Number is: {flo(num1,num2)}")

    else:
        print("invalied operator")

    print("=====================================")

    user_input = input("Do you Want to continoue ? (y/n):")

    if user_input == "n":
        
        break

    

# step 5=dry run 
# num1 = int(input("Enter The first Number:"))=5
# num2 = int(input("Enter The second Number:"))=6
# user=input("Enter Any One operator like +,-,*,/,%,**,//:")=*
# Multification Of Two Number:30







    