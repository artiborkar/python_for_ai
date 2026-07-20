
# Task 9 — Marks List Analyzer

# Ek list marks = [45, 78, 92, 33, 88, 20, 67] lo. Bina max()/min() use kiye (loop se khud nikaalo) print karo:
#  highest, lowest. Phir sum()/len() se average. Aur batao kitne students pass hue (>= 33).
# Concepts: for loop, comparison, running max/min, counter
# Hint: highest = marks[0] se shuru karo, phir loop mein if m > highest: highest = m.


print("==============Marks List Analyzer===========")

marks = [45, 78, 92, 33, 88, 20, 67] 

highest = marks[0]
lowest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

print(f"highest mark :{highest}")

print(f"lowest mark : {lowest}") 

average = sum(marks)/len(marks)
    
print(f"Average is :{average:.2f}")

count = 0

for mark in marks:
    if mark >= 33:
        count += 1
print(count)
