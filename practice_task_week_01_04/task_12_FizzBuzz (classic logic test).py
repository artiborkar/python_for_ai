
# Task 12 — FizzBuzz (classic logic test)
# 1 se 30 tak loop chalao. 3 se divisible → "Fizz", 5 se divisible → "Buzz", dono se → "FizzBuzz",
#  warna number khud print karo.

print("==============FizzBuzz (classic logic test)===============")

for i in range(1,30):
    if i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz")
    elif i % 3 == 0 :
        print("Fizz")
    elif i % 5==0:
        print("Bizz")
    else:
        print(i)
    

