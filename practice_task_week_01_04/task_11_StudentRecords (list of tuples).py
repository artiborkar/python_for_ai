
# Task 11 — Student Records (list of tuples)

# Ek list of tuples banao: [("Asha", 85), ("Rahul", 92), ("Priya", 78)]. Har student ka naam aur marks
#  unpacking se print karo. Phir sabse zyada marks waale ka naam batao.


print("==========Student Records (list of tuples)============")

my_list =  [("Asha", 85), ("Rahul", 92), ("Priya", 78)]

new_tup = tuple([("Asha", 85), ("Rahul", 92), ("Priya", 78)])

print(new_tup)

print(type(new_tup))

a , b, c = new_tup

print(a)

print(b)

print(c)

print(f"Highest marks : {max(new_tup)}")
