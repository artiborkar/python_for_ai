
# Task 12 — FizzBuzz (classic logic test)
# 1 se 30 tak loop chalao. 3 se divisible → "Fizz", 5 se divisible → "Buzz", dono se → "FizzBuzz",
#  warna number khud print karo.

print("=============FizzBuzz (classic logic test)===============")

# for i in range(1,30):
#     if i % 3 == 0 and i % 5 == 0 :
#         print("FizzBuzz")
#     if i % 3 == 0 :
#         print("Fizz")
#     if i % 5:
#         print("Bizz")
#     else:
#         print(i)
    

# for num in range(1,30):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)


for x in range(1,30):
    if x % 3 == 0 and x % 5 == 0 :
        print("FizzBuzz")
        if x % 3 ==0 :
            print("Fizz")
            if x % 5 == 0 :
                print("Buzz")
    else:
        print(x)