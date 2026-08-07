# Project 4 — Greeting Card Maker
# EN: Write a function make_greeting(name, occasion) that returns a message like "Happy Diwali, Asha!". Do NOT print inside the function — return the string and print it outside.
# हिंदी: एक function make_greeting(name, occasion) बनाओ जो "Happy Diwali, Asha!" जैसा message return करे। Function के अंदर print मत करो — string return करो और बाहर print करो।
# Concepts: f-string, return vs print
# Hint: return f"Happy {occasion}, {name}!".

'''
restate 1=make the greeeting
example 2=like,happy hoil arti,happy diwali asha,happy navratri navneet etc
psuedocode 3=1create the function function name is given is make_greeting
             2 parameter is  name, occasion are given 
             3 return the f"Happy {occasion} {name} !"
             4 print the function name and arguments print(make_greeting("Arti", "Holi"))
translate4=
dry run=
def make_greeting(name, occasion):
    "Arti", "Holi"
    return f"Happy {occasion} {name} !
    print(make_greeting("Arti", "Holi"))
Happy Hoil Arti!



'''
print("=====Greeting Card Maker====")

def make_greeting(name, occasion):

    return f"Happy {occasion.title()} {name.title()} !"

print(make_greeting("Arti", "Holi"))


print(make_greeting("vaishnav", "diwali"))