# 
# Ek sentinel _MISSING banake ek function likho jo "given vs not given" bataye.

_MISSING = object()

def new_func(value= _MISSING):
    if value ==  _MISSING :
        print("Not Given")
    else:
        print(f"Given : {value}")

new_func(23)

new_func()

