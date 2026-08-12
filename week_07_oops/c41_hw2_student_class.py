# Ek Student class with name, marks, aur method report() jo report print kare. 2 objects banao.

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def report(self):
        print(f"Name : {self.name} your marks is {self.marks}")


stu_obj1 = Student("Arti Borkar" , 45)


stu_obj2 = Student("Navneet",80)

stu_obj1.report()

stu_obj2.report()