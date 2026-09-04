# Ek Status enum banao (PENDING, DONE, FAILED).
'''
1=restate= Ek Status enum banao (PENDING, DONE, FAILED).
2=example= from enum import Enum, class Status(Enum)
3=psuedocode= 1. import enum from enum import Enum
              2. class is  class Status(Enum)
              3. attribute is PENDING,DONE,FAILED
              4.then print print(Status.PENDING)
              5.attribute value is print(Status.PENDING.value)  
4=transalte=

'''
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    DONE = "done"
    FAILED = "failed"
    

print(Status.PENDING)
print(Status.PENDING.value)   


# dry run 
# print(Status.PENDING.value) 
# class Status(Enum)
# from enum import Enum
#  PENDING = "pending"
# pending