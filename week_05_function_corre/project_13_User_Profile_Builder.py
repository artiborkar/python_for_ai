# Project 13 — User Profile Builder (**kwargs)
# EN: Write show_profile(**details) that prints each detail as key: value. Call it with name, age, and city.
# हिंदी: show_profile(**details) बनाओ जो हर detail को key: value की तरह print करे। इसे name, age, और city के साथ call करो।
# Concepts: **kwargs, dict .items(), loop
# Hint: for key, value in details.items(): print(f"{key}: {value}").

'''
restate1=this program to print the ** kwargs in dict formate
example2=I want the dict in key and value pair like  name, age, and city.this is key 
psuedocode3=1.create the function with function name is  show_profile parameter is (**details)
            2.the apply the for loop is k,v in details.items().
            3.print the f"{k}:{v}
            4.call the function .
transalte4=
dry run 5=
def show_profile(**details) 
for k,v in details.items():
print (f"{k}:{v}")
show_profile(name="Arti",age=21,city="Wardha")
for k,v in details.items():
        print (f"{k}:{v}")
output is name:Arti
age:21
city:Wardha

'''
print("======User Profile Builder (**kwargs)=====")
def show_profile(**details) :
     
    for k,v in details.items():
        print (f"{k}:{v}")

show_profile(name="Arti",age=21,city="Wardha")
