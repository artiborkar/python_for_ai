# Q1
# EN: Two numbers are given. Print their sum. HI: Do numbers diye hain. Unka sum print karo.

# Given: a = 7, b = 5   →  print the total

# step 1 = restate = there are two number are given and output is 12.
# step 2 = Example = a=7,b=5 or sum print
# step 3 = psuedocode = 1.create a two variable
#                       2.first is a=7 2nd var is b=5 is given 
#                       3. then 3rd varible is num_sum
                        # 4. print num_sum
                        # 5.show the answer
# step 4 = Translate

a = 7
b = 5
num_sum = a+b
print(num_sum)

# step 5=dryrun
# step    a      b     num_sum
# 1        7
# 2        7      5      
# 3       7       5      12
# 4     print(num_sum)====12

print("========================")






# Q2
# EN: Two numbers are given. Print the larger one. HI: Do numbers diye hain. Bada wala print karo.

# Given: a = 8, b = 3
#  step 1 = restate = there are two number are given and output is 8.
# step 2 = Example = a=8,b=3 or  print largest number.
# step 3 = psuedocode = 1.create a  variable  a=8 b=3
#                       2.then check the if condtion.   
#                       3. if a>b then print a 
                        # 4. if else then print b
                        # 5.show the answer
# step 4 = Translate =
a=8
b=3

if a>b:
    print (a)
else:
    print (b)


# step 5 =dry run
# step   a   b 
# 1      8    3
# 2     8
        


print("=========================")







# Q3
# EN: A number is given. Print its square. HI: Ek number diya hai. Uska square print karo.

# Given: n = 6

# step 1 = restate = give number 6 print the square is 36.
# step 2 = Example = n=6 sencond veriable is square = 6**2
# step 3 = psuedocode = 1.create a two varible n is given and second is square 
#                      
                        # 4. print square

# step 4 = Translate =
n = 6
square = 6**2
print(square)

# # step 5=dry run 
# step    n    square
# 1        6
# 2        6      36
# print(square)=====36

print("===================")





# Q4
# EN: A number is given. Print "Even" or "Odd". HI: Ek number diya hai. "Even" ya "Odd" print karo.

# Given: n = 9

# step 1 = restate = give number is 9 print the number is even or odd.
# step 2 = Example = n is a varible assign th value is 9
# step 3 = psuedocode = 1. allready given a varible n
#                       2. then check th condtion if a is % 2 then print even 
#                       3 .false then exculted else part odd
#                       4. show the answer.
# step 4 =translate=
n = 9
if a%2==0:
    print("Number is Even")
else:
    print("Number is Odd")


# step 5= Dry run
# step    n   
# 1       9
# if      f
# else    odd
# print===odd

print("=====================")





# Q5
# EN: A number is given. Print "Positive", "Negative", or "Zero". HI: Ek number diya hai. "Positive", "Negative", ya "Zero" print karo.

# Given: n = -4
# step 1 = restate = give number is -4 print the number is +,_,0 number is -.
# step 2 = Example = n is a varible assign th value is -4
# step 3 = psuedocode = 1. our vaiable is n=-4 is given.
#                       2. then check the condtion if n >0 then the print if part
#                       3 .this condtion is false then exculted elif part is n<0
#                       4. this condtion is false then the execulted else part
#                       5. print the answer.
# step 4 =translate=
n = -4
if n > 0:
    print("Number is positive")
elif n < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

# step 5 dry run :
# step   n
# 1      -4
# 2      f
# 3      t
# print()====_Negative

print("================================")





# Q6
# EN: A Celsius temperature is given. Print it in Fahrenheit. (F = C * 9/5 + 32) HI: Celsius diya hai. Fahrenheit mein print karo.

# Given: c = 100
# step 1 = restate = A Celsius temperature is given and  Fahrenheit.print karna hai
# step 2 = Example = n is a varible assign th value is -4
# step 3 = psuedocode = 1. our vaiable is c = 100 is given.
#                       2. 2 nd variable is Fahrenheit. (F = C * 9/5 + 32)
#                       3. print Fahrenheit.

# step 4 =translate=
c = 100
fahrenheit = c * 9/5 + 32
print(fahrenheit )

# step 5 =dry run
# step   c    fahrenheit
# 1     100
# 2     100
# 3     100     212  

print("=================")




# Q7
# EN: A word is given. Print how many letters it has. HI: Ek word diya hai. Usme kitne letters hain print karo.

# Given: word = "python"

# step 1 = restate = given value to check the Print how many letters .
# step 2 = Example = word is a varible assign th value is python
# step 3 = psuedocode = 1.given variable is word = "python".
#                       2. print length of variable.
#                       3. print answer

# step 4 =translate=
word = "python"

print(len(word))

# step 5=dry run 
# word    python  
# 1
# 2       6

# print()========6

print("==========================")







# Q8
# EN: Two names are given. Join them with a space and print. HI: Do naam diye hain. Beech mein space laga kar jodo aur print karo.

# Given: first = "Ravi", last = "Kumar"   →  "Ravi Kumar"
# step 1 = restate = given  first = "Ravi", last = "Kumar" output is Ravi Kumar .
# step 2 = Example = word is a varible assign th value is python
# step 3 = psuedocode = 1.two variable is given and 3rd varible is join_nam = first+last
#                       2. print join_nam.
#                       3. print answer

# step 4 =translate=
first = "Ravi"
last = "Kumar"   

print(f"{first} {last}")

# step 5=Dry run
# step     first     last
# 1        Ravi 
# 2                 Kumar
# 3                 Ravi Kumar
# print(join_nam)====Ravi Kumar

print("=================")






# Q9
# EN: A number is given. Print its last digit. HI: Ek number diya hai. Uska aakhri digit print karo.

# Given: n = 574   →  4
# 1=restate =A number is given. Print its last digit,n = 574   →  4.
# 2=example=ek number given hai 574 hum direct index no. se print krenge
# 3=pseudcode=1.n = 574  
#             2.by print n is divisble  to 10
            #   3.then 574%10====% return the remainder.
#             3.print the result.4
# 4=Translate=
n = 574 
print(n%10)


# 5=dry run 
# step  n
# 1     574
# 2      4
print("===================")






# Q10
# EN: Total seconds are given. Print how many full minutes and leftover seconds. HI: Total seconds diye hain. Kitne poore minutes aur bache hue seconds print karo.

# Given: total = 130   →  2 minutes 10 seconds

# 1=restate =Total seconds are given. Print how many full minutes and leftover seconds.
# 2=example=total = 130  total //60 and total%60 print
# 3=pseudcode=1.given variable is total = 130
#             2.2nd var is minute to check min like total //60 
#             3.3rd var is sec to check sec of total%60

# 4=Translate=
total=130
min_total = total//60
sec_total = total%60
print(f"{min_total} minute \n{sec_total} second")

print("======================")





# Q11
# EN: A number n is given. Print the sum of all numbers from 1 to n. HI: Ek number n diya hai. 1 se n tak sabka sum print karo.

# Given: n = 5   →  1+2+3+4+5 = 15

#  1=restate =A number n is given. Print the sum of all numbers from 1 to n 1+2+3+4+5 = 15
# 2=example=given variable is 5 then applya loop  
# 3=pseudcode=1. n = 5 sum=n
#             2.for loop then check range (1,n+1)
#             3.sum+=n
#             4.print(sum)
# 4=Translate=.
n=5
sum=0
for num in range(1,n+1):
    sum=sum+num
print(sum)

# step 5
# step    n    sum    num
# 1       5     0    
# for 1   5     0     1
#               1
# for 2    5    1     2
#          5    3
# for3     5    3     3
#         5     6
# for 4    5    6     4  
#          5    10
# for 5    5    10     5
#               15
print("===========================")




# Q12
# EN: A list of numbers is given. Print the total. HI: Numbers ki ek list di hai. Total print karo.

# Given: nums = [10, 20, 30, 40]

#  1=restate =A list of numbers is given. Print the total  nums = [10, 20, 30, 40] output 100.
# 2=example=given variable is nums = [10, 20, 30, 40] check loop
# 3=pseudcode=1.  nums = [10, 20, 30, 40] count=0
#             2.for check i in num
#             3.print(i)
#             4.count+1
#             5.print(count)
# step5=translate
 
num= [10, 20, 30, 40]
count=0
for i in num:
    print(i)
    count=count+i
print(count)

# 6.dry run 
# step     num                count    i 
# 1      [10, 20, 30, 40]      0   
# for1      [10, 20, 30, 40]    0       10
#                                      10
#                               10
# for2     [10, 20, 30, 40]    10      20         
#                              30
# for3    [10, 20, 30, 40]     30     30
#                              60
# for 4   [10, 20, 30, 40]     60    40
#                             100


print("=======================")





# Q13
# EN: A list of numbers is given. Count how many are even. HI: Numbers ki list di hai. Kitne even hain ginno.

# Given: nums = [1, 4, 6, 7, 10, 3]

#  1=restate =A list of numbers is given. Count how many are even output is 4,6,10.
# 2=example=given variable is nums = [1, 4, 6, 7, 10, 3]check loop
# 3=pseudcode=1. nums = [1, 4, 6, 7, 10, 3]
#             2.for check i in num i%2==0
#             3.print(i)
#             
# step5=translate

nums = [1, 4, 6, 7, 10, 3]
for i in nums:
    if i%2==0:
        
        print(f"even {i}")

# 6dry run
# step               nums                i
# 1             [1, 4, 6, 7, 10, 3]
# for 1                                  1f
# for2                                    4t
#                                        4
# for 3                                  6t
#                                       6
# for 4                                7 f
# for 5                                10t
#                                     10
# for 6                                3f

print("========================")




# Q14
# EN: A list is given. Find the biggest number without using max(). HI: Ek list di hai. max() ke bina sabse bada number dhoondho.

# Given: nums = [4, 9, 2, 11, 6]

#  1=restate= A list is given. Find the biggest number without using max() is 11
# 2=example=given variable is nums = [4, 9, 2, 11, 6] check loop
# 3=pseudcode=1. nums = [1, 4, 6, 7, 10, 3]
#             2.for then if
#             3.print(i)
#             
# step5=translate
nums = [4, 9, 2, 11, 6]
biggest=0
for num in nums:
    if biggest<num:
        biggest=num
print(biggest)

# 6 dry run
# step       nums               biggest     num
# 1      [4, 9, 2, 11, 6]         0           
# for1                                       4
# if                              4
# for2                                      9
# if2                             9
# for3                                       2
# if 3                             9         f
# for 4                                      11
# if4                              11
# for 5                                      6
# if 5                             11

# print===============11

print("============================")





# Q15
# EN: A word is given. Count the vowels in it. HI: Ek word diya hai. Usme vowels ginno.

# Given: word = "education"

#  1=restate= A word is given. Count the vowels in it is "e u  a i o"
# 2=example=given variable is word = "education" check loop
# 3=pseudcode=1. nums = [1, 4, 6, 7, 10, 3]
#             2.for then if
#             3.print(i)
#             
# step5=translates
word = "education"
count=0
for n in word:
    if n in "aeiou":
        count+=1

        print(n)
# # 6 dry run
# step        word          count          n
# 1          education        0    
# for 1                                      e
# if                           e
# for 2                        e              d
# if 2                         e              f
# for 3                        e              u
# if 3                          u              t
# for 4                        u              c
# if 4                          u              f
# for 5                        u              a
# if 5                          a             t              
# for 5                        a             t
# if 5                          a             f
# for 6                        a              i
# if 6                          i            t   
# for 7                          i             o
# if 7                          o            t 
# for 8                         o             n
# if 8                        o             f    
# print()====e u a i o


print("=================")





# Q16
# EN: Print all even numbers from 1 to 10, each on its own line. HI: 1 se 10 tak saare even numbers print karo, har ek nayi line mein.

# (no input — just 1..10)

#  1=restate= Print all even numbers from 1 to 10, each on its own line.just 1..10
# 2=example= check loop
# 3=pseudcode=1.for loop range (1,10)
#             2.check condtion %2==0
#             3.print
#             
# step5=translates
for num in range(1,10):
    if num%2==0:
        print(num)

# step 6 dry run
# step         num    
# 1            1
# if           f
# f2           2
# if2          t
# f3           3
# if3          f
# f4           4
# if4          t
# f5           5
# if5          f
# f5=6         6
# if6          t
# f7           7
# if7          f
# f8           8
# if8          t
# f9           9
# if9          f

print("========================")




# Q17
# EN: A list of marks is given. Print the average. HI: Marks ki list di hai. Average print karo.

# Given: marks = [40, 55, 70, 90]

#  1=restate= A list of marks is given. Print the average is 63.75..
# 2=example= given marks = [40, 55, 70, 90] then check loop
# 3=pseudcode=1.marks = [40, 55, 70, 90] variable 2 is total=0
#             2.then for excuted
#             3.print
#             
# step5=translates
marks = [40, 55, 70, 90]
total=0
for mark in marks:
    total=total+mark
total_len=len(marks)
avg=total/total_len
print(avg)

# 6.dry run
# step        marks            total     mark      total_len  avg
# 1        [40, 55, 70, 90]     0
# f1                             40         40           4       10
# f2                              95        55           4                   

print("===========================")






# Q18
# EN: A word is given. Build and print its reverse (accumulator = ""). HI: Ek word diya hai. Uska reverse banao aur print karo.

# Given: word = "hello"   →  "olleh"
#  1=restate= A word is given. Build and print its reverse (accumulator = ""),"olleh"
# 2=example= given marks = [40, 55, 70, 90] then check loop
# 3=pseudcode=1.marks = [40, 55, 70, 90] varable 2 is total=0
#             2.then for excuted
#             3.print
#             
# step5=translates
