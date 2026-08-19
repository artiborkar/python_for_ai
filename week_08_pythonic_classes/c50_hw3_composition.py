# Computer class banao jo CPU aur RAM objects rakhe (composition).


# 1=restate=Computer class banao jo CPU aur RAM objects rakhe (composition).
# 2=example=class CPU:,class RAM:,class Computer:
# 3=psuedocode= 1. three class 1st class CPU ,2nd class RAM , 3rd class Computer
#               2. 1st class method processer and print the string 
#               3. 2nd class method memory and print any string.
#               4. 3rd class call the object for CPU OR RAM .
#                5 .self.cpu = CPU(), self.ram = RAM()
#                6. method run call the object and method self.cpu.processer(),self.ram.memory()
#                7. object caomputer = Computer()   and call the run method.
# 4=translate python=

print("--------------homework 3--------------")



class CPU:
    def processer(self):
        print("cpu is processing !")


class RAM:
    def memory(self):
        print("ram is an memory ! ")
    

class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()

    def run (self):
        self.cpu.processer()
        self.ram.memory()


computer = Computer()

computer.run()

# 5=dry run =
# 1.computer = Computer()
# 2.def __init__(self):
#         self.cpu = CPU()
#         self.ram = RAM()
# 3.def run (self):
#         self.cpu.processer()
#         self.ram.memory()
# 4.def processer(self):
#         print("cpu is processing !")
#  def memory(self):
#         print("ram is an memory ! ")