
# Task 15 — Duplicate Remover (order preserve)
# Ek list nums = [3, 1, 2, 3, 4, 1, 5, 2] lo. Duplicates hatao par original order bana rahe. 
# (Sirf set(nums) order tod dega — isliye set ko sirf "dekha kya" check ke liye use karo.)

# Concepts: set for membership, list, for loop, .append()
# Hint: ek seen = set() rakho. Har num par: agar num not in seen, toh result mein append karo aur seen.add(num).

print("======= Duplicate Remover (order preserve)========")

nums = [3, 1, 2, 3, 4, 1, 5, 2]

seen = set()

for num in nums :
    
    num not in seen 
    print(num.append(seen))

# new_set = set(nums)

# print(new_set)

# print(nums)