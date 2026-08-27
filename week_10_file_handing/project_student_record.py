# Task
# Ek Python program banao jo:
# Student ka name, age, marks le.
# Student records ko list of dictionaries mein store kare.
# Records ko students.json file mein save kare.
# JSON file se records load kare.
# Loaded students ko print kare.
# 90 se zyada marks wale students ko print kare.

import json



#Student ka name, age, marks le., Student records ko list of dictionaries mein store kare.

student_record = [
                     {
                        "name" : "Arti" , 
                        "age" : 21 , 
                        "marks" : 85
                     },

                     {
                        "name" : "Navneet" , 
                        "age" : 15 , 
                        "marks" : 80
                     },

                       {
                        "name" : "Vaishnav" , 
                        "age" : 17 , 
                        "marks" : 95
                     }

]

# Records ko students.json file mein save kare.
with open("student.json","w") as f:
   json.dump(student_record , f , indent=2)


# JSON file se records load kare.
with open("student.json" , "r") as f:
   student_record = json.load(f)


#  Loaded students ko print kare.
   print(student_record)


# 90 se zyada marks wale students ko print kare.

for student in student_record:
   if student["marks"] > 90 :
      print(student["name"])



