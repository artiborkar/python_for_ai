def my_python():
    print("Hello Python!")

my_python()
print("===============")

##multiple time function call

def my_name():
    print("Hello Arti!")
my_name()
my_name()
my_name()
my_name()
my_name()

print("=================")
#repitly 
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

print("====================")

#input 
temp = int(input("Enter Your tempture:"))
celsius = (temp - 32) * 5 / 9
print(f"{celsius:.2f}")

print("================")

#with functon
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))
print("===============")


#with return
# def fahrenheit_to_celsius(fahrenheit):
#     print(fahrenheit - 32) * 5 / 9
    
# fahrenheit_to_celsius(77)


#with parameter
def my_name(name):
    print("Hello ,",name)
my_name("Arti")

#multiple parameter
def my_name(name):
    print("Hello ,",name)
my_name("Arti")
my_name("Pooja")
my_name("Navneet")
my_name("Sagar")
my_name("Vaishnav")