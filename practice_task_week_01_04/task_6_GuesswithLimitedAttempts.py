
# Task 6 — Guess with Limited Attempts

# Ek secret number fix karo (secret = 42). User ko sirf 3 chances do guess karne ke. Har galat guess par 
# "Too high" / "Too low" batao. 3 ke andar sahi → "You won", warna → "Game over, number was 42".

# Concepts: while, break, counter, if/elif/else
# Hint: attempts counter rakho, while attempts < 3. Sahi guess par break.

print("=============Guess with Limited Attempts================")

secret_number =  42
attempt = 3

user = int(input("Enter the Number : "))

while attempt <= 3:

    if secret_number == user :
        print("congratulations You won")
        break
        
    elif secret_number <= user and secret_number >= user  :
        print("Too high/Too low") 
        break 

else:
    print("game over, number was 42")
    
    break
