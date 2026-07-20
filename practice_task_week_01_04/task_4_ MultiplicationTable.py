
# Task 4 — Multiplication Table (clean)

# User se ek number n aur ek limit k lo. n ka table 1 se k tak print karo (loop se).


print("====== Multiplication Table (clean)======")

n = int(input("Enter the Table Number: "))

k = 0

for i in range(1,11):
    print(f"{n}*{i} = {i*n}")
    k+=i
