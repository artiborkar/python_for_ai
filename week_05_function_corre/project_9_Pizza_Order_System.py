# Project 9 — Pizza Order System (defaults + keyword args)
# EN: Write order_pizza(item, qty=1, size="medium"). Show 3 orders: only item; item + qty; item + size="large" using a keyword argument.
# हिंदी: order_pizza(item, qty=1, size="medium") बनाओ। 3 orders दिखाओ: सिर्फ़ item; item + qty; और item + size="large" keyword argument से।
# Concepts: multiple defaults, positional vs keyword arguments
# Hint: return f"{qty} {size} {item}". Try order_pizza("pizza", size="large").

print("==========Pizza Order System (defaults + keyword args=======")

def order_pizza(item, qty=1, size="medium"):

    return f"{qty} {size} {item}"

print(order_pizza("pizaa"))

print(order_pizza("pizaa",2))

print(order_pizza("pizaa",2,"large"))


'''
restate1=Write order_pizza(item, qty=1, size="medium"). Show 3 orders: only item; item + qty; item + size="large" using a keyword argument.
example2=return f"{qty} {size} {item}" output  1 medium pizaa 2 medium pizaa 2 large pizaa
psuedocode3=
'''