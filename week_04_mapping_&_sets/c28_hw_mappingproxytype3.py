# class 28
# HOMEWORK

# Ek config dict banao, use MappingProxyType se lock karo, padhne ki koshish (chalega) aur badalne ki koshish (error padho).

print("==========Q3.==========")

from types import MappingProxyType

config = {"phone" : "iphone" , "storage" : 168 , "time" : "am"}

data_locked = MappingProxyType({"phone" : "iphone" , "storage" : 168 , "time" : "am"})

print(data_locked)

config["phone"]="vivo"

print(config)


# data_locked["phone"]="vivo"

# print(data_locked)                       #TypeError: 'mappingproxy' object does not support item assignment