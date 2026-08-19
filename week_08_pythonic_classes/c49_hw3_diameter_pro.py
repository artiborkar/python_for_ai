
#Circle mein diameter property banao (2 * radius).

# 1=restate=Circle mein diameter property banao (2 * radius). 
# 2=example=class Circle:,c=Circle(4),print(c.diameter)
# 3=psudocode=1.write the class Circle: method def __init__(self,radius):, 
#             2. create the property and method is diameter.
#             3.object is c and call the class ,c=Circle(4)
#             4.print method
# 4=translate=



print("-------------homework3--------------")

class Circle:

    def __init__(self,radius):
        self.radius=radius

    @property
    def diameter(self):
        return 2*self.radius

c=Circle(4)

print(c.diameter)

# 5=dry run=
# 1.c=Circle(4)
# 2.def __init__(self,radius):
#         self.radius=radius

# 3.print(c.diameter)
# 4.def diameter(self):
#         return 2*self.radius