
print("------------check_grade--------------")

mark=input("Enter your Marks : ")

if mark == "A":
    print("Student was absent")
elif (mark >= str(80)):
    print("grade a")
elif (mark >= str(70)) and (mark < str(80)):
    print("Grade b")
elif (mark >= str(60)) and  (mark < str(70)):
    print("Grade c")
elif (mark >= str(50)) and (mark < str(40)) :
    print("grade d")
elif (mark > str(40)) :
    print("fail")