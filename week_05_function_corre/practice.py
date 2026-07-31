
#  Ek sentinel _MISSING banake ek function likho jo "given vs not given" bataye.
__MIISING = object()

def value(letter=__MIISING):
    if letter is __MIISING:
        return "not given"
    else:
        return f"given {letter}"

print(value(4))

print(value())