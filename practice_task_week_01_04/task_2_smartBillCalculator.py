# Task 2 — Smart Bill Calculator

# Ek item ka price aur quantity maango. Total nikaalo. Agar total 1000 se zyada hai toh 10% discount lagao, 
# warna koi discount nahi. Final amount 2 decimals ke saath print karo.

print("===Smart Bill Calculator===")

items_price = int(input("Enter the price : "))

items_quantity = int(input("Enter the Item Quantity : "))

total = items_price / items_quantity

print(f"Total is :{total}")

if total > 1000:
    print("10% discount")

else:
    print(f"Final Amount : {total:.2f}")

print("==========Thank you==========")