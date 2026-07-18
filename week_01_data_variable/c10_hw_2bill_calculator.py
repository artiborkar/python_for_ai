# Homework

# Ek simple bill calculator: item price aur quantity poochho, total ₹ aur 2 decimals ke saath print karo.

print("===================Q2.==================")

item = input("Enter the Item Name : ")

price = int(input("Enter price :"))

quantity = int(input("Enter Quantity: "))

total = price * quantity

print("=======simple bill calculator=======")

print(f"Item Name : {item}\nPrice :{price}\nQuantity : {quantity}\nTotal price :{total:.2f}")

print("==========================")