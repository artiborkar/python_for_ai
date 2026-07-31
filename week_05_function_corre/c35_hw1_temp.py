
# Apne purane temperature converter (Week 1) ko ek function celsius_to_f(c) mein badlo.

def celsius_to_f(c):
    f= (c * 9 / 5) + 32
    return f"{c} 0c = {f} 0f"

print(celsius_to_f(4))