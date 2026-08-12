# Employee parent with work(); Developer aur Designer children jo alag-alag work print karein.

# 1=resate=Employee parent with work(); Developer aur Designer children jo alag-alag work print karein.
# 2=example=class Employee ,class Developer(Employee),class Designer(Employee)
# 3=psuedocode=1. parent class employee method work
                # 2.child class developer method work
                # 3.child class designer method work.
                # 4.list is emp_list = [Developer(),Designer(),Employee()]
                # 5.apply for emp in emp_list:emp.work()
# 4=translate=
# 5=dryrun=
# emp_list = [Developer(),Designer(),Employee()]

# for emp in emp_list:
#     # emp.work()


print("----------HOMEWORK-------------")

'''
create the parent class is employee 
    method is 
        work :work of the employee

create child class Developer with parent (Employee)
    method is 
        work :work of the developer

create child class Designer with parent (Employee)
    method is 
        work :work of the designer
    
'''

class Employee:
    def __init__(self) -> None:
        pass
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def work(self):
        print("Developer develop  apps")

class Designer(Employee):
    def work(self):
        print("Designer design the page or website")


emp_list = [Developer(),Designer(),Employee()]

for emp in emp_list:
    emp.work()