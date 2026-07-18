# 
# Homework
# Ek program banao jo name aur birth year poochhe, phir age print kare.

print("===========Q1.=============")

name = input("Enter your Name : ").title()

birth_year = int(input("Enter your Birth year :"))

now_year = int(input("Enter the now year :"))

print("=================INFORMATION=============")

print(f"Name : {name}\nBirth Year :{birth_year}\nAge is {now_year - birth_year}")


print("==============================")