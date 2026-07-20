
# Task 7 — Word & Character Counter

# User se ek sentence lo. Print karo: kitne words hain, kitne characters (spaces chhod kar), aur sentence UPPERCASE mein.
# Concepts: .split(), .replace(), len(), .upper(), .strip()
# Hint: spaces hatane ke liye .replace(" ", "") phir len().

print("============Word & Character Counter==============")

user = input("Write a one scentace:")

print(user.split())

print(user.replace(" "," "))

print(len(user))

print(user.upper())

print(user.strip())