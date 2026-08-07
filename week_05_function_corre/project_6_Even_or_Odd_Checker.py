# Project 6 — Even or Odd Checker
# EN: Write a function is_even(n) that returns True if the number is even, else False. Use it in a loop to print which numbers in [3, 8, 15, 22, 41] are even.
# हिंदी: एक function is_even(n) बनाओ जो number even होने पर True, वरना False return करे। इसे loop में इस्तेमाल करके बताओ [3, 8, 15, 22, 41] में कौन-से numbers even हैं।
# Concepts: returning a boolean, %, using a function in a loop
# Hint: return n % 2 == 0.


print("================Even or Odd Checker===========")

def is_even(n):
    
    return n % 2 == 0

num=[3, 8, 15, 22, 41]

for letter in num:
    if is_even(letter):
        print(f"{letter} True")
    else:
        print(f"{letter} False ")


