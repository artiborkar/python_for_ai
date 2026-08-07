# Project 18 — Grade Report (one function, many students)
# EN: Write get_grade(marks) returning "A"/"B"/"C"/"D". Then loop over a dict of students {"Asha": 92, "Rahul": 70, "Priya": 81} and print each student's grade using the function.
# हिंदी: get_grade(marks) बनाओ जो "A"/"B"/"C"/"D" return करे। फिर students के dict {"Asha": 92, "Rahul": 70, "Priya": 81} पर loop चलाकर हर student का grade function से print करो।
# Concepts: return, if/elif/else, reusing a function in a loop, dict .items()
# Hint: >= 90 → A, >= 75 → B, >= 60 → C, else D.




print("======Grade Report====")

def get_grade(marks):

    

    if marks >= 90:
        return "Grade A"
    elif marks >= 75:
        return "Grade B"
    elif marks >= 60:
        return "Grade C"
    else:
        return "Grade D"
    
student=({"Asha": 92, "Rahul": 70, "Priya": 81})

for name , mark in student.items():
    grade=get_grade(mark)
    print(f"{name}:mark={mark} {grade}")

