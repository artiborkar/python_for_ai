# Student class mein __str__ add karo jo "NAME scored MARKS" de.


# 1=restate=student class mein __str__add karo jo "NAME scored MARKS" de.
# 2=example=class Student:,def __str__(self):
# 3=psuedocode=1.write the class Student,
#              2.method def__init__(self,name,marks)
#              3.self.name=name,self.marks=marks
            #  4.2nd special method def __str__(self)
            #  5.return f"NAME {self.name} Scored Marks is {self.marks}
            #    6.create the object and print the object
# 4=translate=

print("-------homework1-----------")

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __str__(self):
        return f" {self.name} Scored {self.marks}"


student=Student("Arti",78)

print(student)


# 5=dry run=
# 1.student=Student("Arti",78)
# 2.def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
# 3.print(student)
# 4.def __str__(self):
#         return f"NAME {self.name} Scored MARKS is {self.marks}"


