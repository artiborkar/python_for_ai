# Project 8 — Smart Greeting (default value)
# EN: Write greet(name, greeting="Hello") where greeting has a default. Call it once with only a name, and once with a custom greeting like "Namaste".
# हिंदी: greet(name, greeting="Hello") बनाओ जिसमें greeting का default हो। इसे एक बार सिर्फ़ name के साथ, और एक बार custom greeting जैसे "Namaste" के साथ call करो।
# Concepts: default parameter value
# Hint: return f"{greeting}, {name}!". Calling greet("Asha") uses the default.


'''
restate1=write  greet(name, greeting="Hello") where greeting has a default. Call it once with only a name, and once with a custom greeting like "Namaste".
example2=return  f"{greeting.upper()}, {name.upper()}!" is given HELLO, ARTI! , NAMASTE, ARTI! output.
psuedocode3=1create a function greet(name, greeting="Hello")
            2:return  f"{greeting.upper()}, {name.upper()}
            3:print(greet("Arti")),print(greet("Arti","Namaste"))
            4:output HELLO, ARTI! , NAMASTE, ARTI!
translate4=
dry run 5=
def greet(name, greeting="Hello")
greet("Arti")
f"{greeting.upper()}, {name.upper()}!
greet("Arti","Namaste")
 f"{greeting.upper()}, {name.upper()}
  HELLO, ARTI! , NAMASTE, ARTI!

'''


def greet(name, greeting="Hello"):

    return  f"{greeting.upper()}, {name.upper()}!"


print(greet("Arti"))

print(greet("Arti","Namaste"))