# Employee parent (name, salary); Manager child jo super() use kare aur ek team_size add kare.

# 1=resate= Employee parent (name, salary); Manager child jo super() use kare aur ek team_size add kare.
# 2=example= create the parent class Employee and child class is manager
# 3=psuedocode=1.create the parent class Employee method is special method _init__ attribute  self.name ,self.salary
            #  2.create child class is Manager  with empolyee attribute is  self.team_size methood is call the parent class
            #  3.create the object manager_obj = Manager("Arti Borkar",100000,10)
            #  4.print the parameter
# 4=translate=
# 5=dryrun=
# manager_obj = Manager("Arti Borkar",100000,10)
# class Employee:
#     def __init__(self,name:str,salary:float):
        # self.name = name
        # self.salary = salary

# print(manager_obj.name)
# print(manager_obj.salary)
# print(manager_obj.team_size)

print("------------HOMEWORK----------------")

'''
create the class of parent is Employee:
    attribute :
        name:name of the employee
        salary:salary of the employee
    method:
        speciaal method is __init

create child class is manage with employee.
    attribute:
        team_size = memeber of the team
    method:
        call the parent class

create the object

'''

class Employee:
    def __init__(self,name:str,salary:float):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self,name:str,salary:float,team_size:int):
        super().__init__(name,salary)
        self.team_size = team_size

    
manager_obj = Manager("Arti Borkar",100000,10)
print(manager_obj.name)
print(manager_obj.salary)
print(manager_obj.team_size)
