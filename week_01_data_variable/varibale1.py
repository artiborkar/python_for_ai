# class 6 homework
student_name = "Arti Borkar"

student_age = 21

student_city = "Wardha"

favourite_subject = "Python"

dream_job = "AI Engineer"

print(student_name)

print(student_age)

print(student_city)

print(favourite_subject)

print(dream_job)


# class 7 homework

radius = 7

area = 3.14159 * radius ** 2

print(area)                 

marks = 425

total = 500

percentage = marks / total * 100

print(percentage)           

print(2026 % 4)             


# class 8 homework
name = "Arti"

city = "Wardha"

print(f"Hi, I am {name} from {city}.")

cost = 250

qty = 4

print(f"Total is {cost * qty} rupees")

marks = 367

print(f"Percentage: {marks / 450 * 100:.2f}%")



# class 9 homework

is_sunny = True

is_weekend = False

print(is_sunny and is_weekend)   

print(is_sunny or is_weekend)   

print(not is_weekend)           

num = int("45")

print(num + 5)                   

print(10 == 10.0)                

print(int(7.8))      


# class 10 homework
# mini project  1 Temperature Converter

print("=== Celsius to Fahrenheit Converter ===")

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C = {fahrenheit}°F")



# mini project  2 AI Token Cost Estimator
print("=== AI Token Cost Estimator ===")

tokens = int(input("How many tokens? "))

price_per_1000 = float(input("Price per 1000 tokens (in rupees)? "))

cost = (tokens / 1000) * price_per_1000

print(f"Estimated cost: ₹{cost:.2f}")


# Homework
print("=== Homework ===")
name = input("Name: ")

birth_year = int(input("Birth year: "))

print(f"{name}, you are about {2026 - birth_year} years old")

# 2

price = float(input("Price: "))

qty = int(input("Quantity: "))

print(f"Total: ₹{price * qty:.2f}")

# 3
msg = input("Type a sentence: ")
print(msg.strip().upper())
