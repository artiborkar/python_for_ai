# Task 3 — Even ya Odd + Positive/Negative

# User se ek number lo. Batao woh positive/negative/zero hai, AUR even/odd hai (zero ke liye even/odd mat batao

print("===Even ya Odd + Positive/Negative===")

num = int(input("Enter the Number :"))

if num > 0:
    print(f"Number is Positive ")
    if num % 2 ==0:
        print(f"Number is Even")
    else:
        print(f"Number is odd")


elif num < 0:
    print(f"Number is  Negative")
    
else: 
    print(f"Number is Zero ")
