# # User class mein from_dict classmethod banao.

# 1=restate=User class mein from_dict classmethod banao.
# 2=example=class User ,def __init__(self,name,age):,@classmethod
# 3=psuedocode=1.class User with special method def __init__(self,name,age):
             # 2. @classmethod decorator then methoddef from_dict(cls,data):return cls(data["name"],data["age"])
        #      3.object and call the class with method  user=User.from_dict({"name":"Arti","age":21})
        #       4.print(user.name,user.age)
#4=translate python=

print("---------homework 3----------")
class User :
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod

    def from_dict(cls,data):
        return cls(data["name"],data["age"])
        

user=User.from_dict({"name":"Arti","age":21})

print(user.name,user.age)

# print(user.age)

# 5=dry run=
#1. user=User.from_dict({"name":"Arti","age":21})
# 2.def __init__(self,name,age):
        # self.name=name
        # self.age=age

# 3.print(user.name,user.age)
# 4.def from_dict(cls,data):
        # return cls(data["name"],data["age"])