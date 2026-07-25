# Write a program that prints "Hello, World!".
print("Hello,World!.")

print("===================================")

# Take a user's name as input and print a greeting.
user_name=input("Enter Your Name:").title()
print(f"Hello,{user_name}")

print("================================")

# Find the sum of two numbers entered by the user.
num1=int(input("Enter The First Number:"))
num2=int(input("Enter The Second Number:"))
print(f"Sum Of Two Number {num1+num2}")

print("========================")

# Check whether a number is even or odd.
for i in range(1,20):
    if i%2==0:
        print(f"Even: {i}")
    else:
        print(f"Odd : {i}")

# comprehension
even_odd = [i for i in range(1,20) if i%2==0]
print(even_odd)

print("=============================")

# Find the largest of three numbers.

print("====================")

x = 10
y = 5
print(x + y)

print("=========================")

# Question 2

a = 7
a = a + 3
print(a)

print("===============================")

# Question 3

num = 8
if num > 5:
    print("Big")
else:
    print("Small")


print("===========================")

# Question 4

for i in range(5):
    print(i)

print("========================") 

# Question 5
s = 0
for i in range(1, 6):
    s = s + i
print(s)

print("===================")

# Question 6

s = 0
for i in range(1, 6):
    if i % 2 == 0:
        s = s + i
print(s)

print("=======================")
# Question 7

for i in range(2, 10, 2):
    print(i)

print("==========================")

# Question 8

count = 0
for i in range(5):
    count += i
print(count)

print("================================")


# Question 9

for i in range(5, 0, -1):
    print(i)

print("===================")

# Question 10

x = 1
for i in range(4):
    x = x * 2
print(x)

print("===============================")

# Level 3: Nested Loops ⭐⭐⭐


# Question 11

for i in range(2):
    for j in range(3):
        print(i, j)

print("=============================")

# Question 12

count = 0
for i in range(3):
    for j in range(2):
        count += 1
print(count)

print("========================")

# Question 13

for i in range(1, 4):
    for j in range(i):
        print("*", end="")
    print()

print("=============================")

# Level 4: While Loop ⭐⭐⭐


# Question 14

i = 1
while i <= 5:
    print(i)
    i += 2

print("===============================")

# Question 15

n = 10
while n > 0:
    n -= 3
    print(n)


print("================================")

# Question 16

x = 1
while x < 20:
    x = x * 3
print(x)

print ("===========psudocode==============")

#1. User se do numbers input lo aur unka sum print karo.
# 1)Restate = user se don number lo or sum print 
# 2) Example = create 3 variable a, b,c  then print sum .
# 3)psudocode = 1.create varible a is a=int(input("enter num:"))
#               2. create varible two is b=int(input("enter num2"))
#               3. 3 rd variable is c =a+b
#               4.  print (c)
# 4)
a = int(input("Enter The First Number:"))
b = int(input("Enter The Second Number:"))
c = a+b
print(f"Sum Of Two Number:{c}")

# 5)
# step    a   b    c
# 1       4   
# 2       4    5  
# 3       4    5    9
# print(c)===9



print("=======================")
# 2.Check karo ki number even hai ya odd.
# 1)restate= number even ya odd 
# 2)example= num is 20 output is even
# 3)psudocode=1.ek variable lo us mai ek value store karo
            # 2. if condtion chalako or tekho num%2==0 the value is true then the print even 
            # 3.if excuted else part then print odd 
#4)translate=
num = 20 
if num%2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# 5)dry run =
# step       num 
# 1         20
# 2          20%2   t
# 3           20

print("========================")

# 3. Teen numbers me se sabse bada number find karo.
#  1)restate= 3 number me se sabse bda number find karo.
# 2)example= a=29,b=3,c=90
# 3)psudocode=1.a,b,c=29,3,90
            # 2.4 variable is big_num=0
            # 3.if check 
            


# 1 se 100 tak ke numbers print karo.
# Kisi number ka multiplication table print karo.
# Factorial of a number calculate karo.
# Prime number check karo.
# Fibonacci series print karo.
# String ko reverse karo.
# Palindrome string check karo.
