
# Task 16 — Two Class Comparison (sets)
# Do sets banao: python_students aur java_students (kuch naam dono mein common ho). Print karo: (a) dono seekhne wale, 
# (b) sirf Python, (c) total unique students, (d) sirf ek language seekhne wale.

# Concepts: set operations &, -, |, symmetric difference ^
# Hint: "sirf ek language" = python ^ java (symmetric difference).

print("===========Two Class Comparison (sets)=============")

python_students = {"Arti","Rohini","Shreya","Diksha","Pooja"}

java_students = {"Navneet","Diksha","Vaishnav","Arti","Sagar"}

a = python_students & java_students

print(f"dono lang seekhne wale {a}")

b = python_students ^ java_students

print(f"sirf python seekhne vale {b}")

c = python_students | java_students 

print(f"Total unique student {c}")

d = python_students - java_students 

print(f"sirf ek lang seekhne vale {d}")