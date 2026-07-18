# Task 1 — Personal Profile Card.

# User se name, age, city, aur favourite_subject maango (input()). Phir ek saaf profile card f-string se print karo.

print("==========profile card==============")

user_name = input("Enter Your Name : ")

user_age = int(input("Enter Your Age : "))

user_City = input("Enter Your City : ")

favourite_subject = input("Enter Your favourite_subject :")

print("==========profile card==============")

# print(f"Your Name is = {user_name}\nYour Age is = {user_age}\n your City = {user_City }\n your favourite_subject is = {favourite_subject }")

# print(f"Your Name is = {user_name}\nYour Age is = {user_age}")

# print(f"Your City = {user_City }\nYour favourite_subject is = {favourite_subject }")


print(f" Name : {user_name.title()}")

print(f" Age : {user_age}")

print(f" City  : {user_City.title()}")

print(f" favourite_subject : {favourite_subject.title()}")

print("=============================================")