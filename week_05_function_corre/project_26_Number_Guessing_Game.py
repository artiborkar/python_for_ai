# Project 26 — Number Guessing Game (refactored)
# EN: Refactor the guessing game into functions: check_guess(guess, secret) returns "low"/"high"/"correct", 
# and play(secret, max_attempts) runs the whole game loop using it, returning True if the player won. Print win/lose with attempts used.
# हिंदी: guessing game को functions में बाँटो: check_guess(guess, secret) जो "low"/"high"/"correct" return करे, और play(secret, max_attempts) जो पूरा game loop चलाए और जीतने पर True return करे। कितने attempts लगे उसके साथ win/lose print करो।
# Concepts: helper functions, while, counter, return a boolean
# Hint: Loop while attempts < max_attempts; on "correct" return True; after loop return False.




print("=====Number Guessing Game======")

def check_guess(guess, secret):

    if guess < secret:
        return "low"
    elif guess > secret:
        return "high"
    else:
        return "Coreect"
    
# print(check_guess(34,40))

# print(check_guess(60,50))

# print(check_guess(70,70))

print("----------------------------")

def play(secret, max_attempts):

    attempts = 0
    while attempts < max_attempts:
        guess_num=int(input("Enter the number:"))
        result=check_guess(guess_num,secret)
        attempts+=1
        if result=="correct":
            print("win")
            return True
        elif result=="low":
            print("low")

        else:
            print("high")

    print("win/lose")
    return False

# user_input=input("Do you want to continoue(y/n):")
# if user_input==0:
    # break
won =play(12, 3)
print(won)
