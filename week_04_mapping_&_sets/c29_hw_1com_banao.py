# class 29
# Homework

# 1–20 ke saare numbers ka comprehension banao, sirf woh jo 3 se divisible hain.

num_comprehension = [ num for num in range(1,21) if num % 3 == 0]

print(num_comprehension)

num_comprehension_set = {n  for n in range(1,21) if n % 3 == 0}

print(num_comprehension_set)