
# Task 8 — Reverse & Palindrome Check

# User se ek word lo. Use ulta print karo, aur batao woh palindrome hai ya nahi 
# (case ignore karo — "Madam" bhi palindrome hai).

print("============ Reverse & Palindrome Check=============")

user = input("Enter the word :")

print(user[::-1])

if user==user[::-1] :
    print("palindrome")
else:
    print("Not palindrome")

