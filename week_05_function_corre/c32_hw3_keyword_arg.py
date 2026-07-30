# Ek function ko keyword arguments se call karke dikhao (order badal kar).

def key_arg(name,age,city):

    return f"{name} {age} {city}"

print(key_arg("Arti",21,"Wardha"))

print(key_arg(name="Arti",age=21,city="Wardha"))

print(key_arg(age=21,city="Wardha",name="Arti"))