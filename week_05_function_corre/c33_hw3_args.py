# greet_all(*names) jo har naam ko "Hello NAME" print kare (loop se).

def greet_all(*names):

    for word in names:
    
        print (f"HELLO {word.upper()}")

greet_all("Arti","Navneet")


greet_all("xyz")



