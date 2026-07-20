
# Task 5 — Sum & Average of N Numbers

# User se pehle poochho kitne numbers dega (count). Phir loop mein ek-ek karke numbers lo, unka sum aur average print karo.

print("=======Sum & Average of N Numbers========")

count = int(input("kitne numbers chahiye ? : "))

total = 0

for i in range(count):
    num = int(input(f"number{i+1}:"))
    total+=num

avg = total/count

print(f"sum:{total}")

print(f"average :{avg}")