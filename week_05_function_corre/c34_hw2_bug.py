# Jaan-boojh kar def f(x=[]) waala bug banao, 3 call karke bug dikhao.

def f(text,x=[]):
    x.append(text)
    print (x)

f("Arti")

f("Vaishnav")

f("Navneet")