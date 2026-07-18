
# Task 9 — Marks List Analyzer
# Ek list marks = [45, 78, 92, 33, 88, 20, 67] lo. Bina max()/min() use kiye (loop se khud nikaalo) print karo:
#  highest, lowest. Phir sum()/len() se average. Aur batao kitne students pass hue (>= 33).

print("==============Marks List Analyzer===========")

marks = [45, 78, 92, 33, 88, 20, 67] 

for mark in marks:
    print(mark)

print(f"length of list :{len(marks)}")

average = sum(marks)/len(marks)
    
print(f"Average is :{average}")

if average >= 33:
    print("mark")                    #incomplete