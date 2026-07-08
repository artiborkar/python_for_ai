
import random



print("=============Welcome to the Number Guessing Game==========")

while True :   
    secret_number = random.randint(0,100)

    for i in range (0,5):

        print(f"Attempt {i+1} of 4")
        user_guess_num = int(input("Enter the Guess number [0-9]:"))
        if user_guess_num  == secret_number :
            print(f"Congragulations! you have guessed the number in (i+1) attempts")
            break
        if  user_guess_num > secret_number :
            print("Too high try again.")
        elif user_guess_num < secret_number :
            print("Too low ! Try again.")

        print("==================")

    print("the secret number was :",secret_number)

    print("*"*50)
    user_input=input("Do you want to play again ?(yes/no):")
    if user_input=="no":
        break