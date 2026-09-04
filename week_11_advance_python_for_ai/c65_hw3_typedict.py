# Ek TypedDict User banao (name: str, age: int).

'''
1=restate= Ek TypedDict User banao (name: str, age: int).
2=example=  from typing import TypedDict,print(user)
3=psuedocode=  1.from typing import TypedDict
               2. create a class class User(TypedDict)
               3. attribute is name: str, age: int
               4.store the data user = User={"name":"arti","age":21}
               5.print(user)
4=translate in python=
'''

from typing import TypedDict

class User(TypedDict):
    name : str
    age : int


user = User={"name":"arti","age":21}

print(user)


# dry run 
# print(user)
# user = User={"name":"arti","age":21}
# class User(TypedDict)
# from typing import TypedDict
# name: str, age: int