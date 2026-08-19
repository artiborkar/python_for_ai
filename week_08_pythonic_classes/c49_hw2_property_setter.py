# Person class mein age property + setter jo negative age reject kare.


# 1=restate= Person class mein age property + setter jo negative age reject kare.
# 2=example=class Person:, method def __init__(self,age=1)
# 3=psuedocode=class Person:, method def __init__(self,age=1): attribute self.age=age
            # 2.@property,def age(self):,return self._age
            # 3.@age.setter,def age(self,value):,if value<0,raise ValueError("Age is reject beacause age is negative "),self._age=value
            # 4.p=Person(20),print(p.age),p=Person(-9),print(p.age)
# 
# 4=translate python=

print("-----------homework 2-------------")
class Person:
    def __init__(self,age=1):
        self.age=age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if value<0:
            raise ValueError("Age is reject beacause age is negative ")

        self._age=value

p=Person(20)

print(p.age)

p=Person(-9)

print(p.age)


# 5=dry run=