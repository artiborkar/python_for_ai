# Project 20 — Build Your First Tools Library (capstone)
# EN: Create a file my_tools.py with 4 reusable functions, each returning a value: celsius_to_f(c), bmi(weight, height), is_prime(n), and word_count(text). Test all four and print the results. This is the seed of your own "AI tools" library!
# हिंदी: एक file my_tools.py बनाओ जिसमें 4 reusable functions हों, हर एक value return करे: celsius_to_f(c), bmi(weight, height), is_prime(n), और word_count(text)। चारों को test करके results print करो। यह आपकी अपनी "AI tools" library की शुरुआत है!
# Concepts: multiple functions, return, loops/flags inside functions, .split()
# Hint: For is_prime, use a flag: assume prime, loop 2..n-1, if any divides evenly set flag False. For word_count, return len(text.split()).



print("========Build Your First Tools Library======")

print("--------------(1)-------------")

# def celsius_to_f(c):

#     return (c * 9 / 5) + 32


# print(celsius_to_f(45))

# print("---------------(2)------------")


# def bmi(weight, height):

#     return weight / height ** 2

# print(bmi(2000,5))


# print("------------(3)---------------")


def is_prime(n):

    if n <= 1:
        return "not prime"

    for i in n:
        if n % i == 0:
            return "not prime"
    
    return "prime"


print(is_prime(2))
print(is_prime())

print("------------(4)---------------")


# def word_count(text):

#     return len(text.split())

# print(word_count("Arti"))
# print(word_count("I am study in python for i want the agentic Ai engineer"))

# print("---------------------------")