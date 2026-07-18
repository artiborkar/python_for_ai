
# Task 16 — Two Class Comparison (sets)
# Do sets banao: python_students aur java_students (kuch naam dono mein common ho). Print karo: (a) dono seekhne wale, 
# (b) sirf Python, (c) total unique students, (d) sirf ek language seekhne wale.

# Concepts: set operations &, -, |, symmetric difference ^
# Hint: "sirf ek language" = python ^ java (symmetric difference).

print("===========Two Class Comparison (sets)=============")

python_students = {"Arti","Rohini","Shreya","Diksha","Pooja"}

java_students = {"Navneet","Diksha","Vaishnav","Arti","Sagar"}

a = python_students & java_students

print(a)

print(python_students)

c = python_students | java_students 

print(c)

d = python_students - java_students 

print(d)