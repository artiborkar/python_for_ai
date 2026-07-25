#  Homework — Pehle pseudocode likho (kaagaz), PHIR code
# Ek number lo aur batao woh positive, negative ya zero hai.

# step 1 = restate = Ek number lo aur batao woh positive, negative ya zero hai.
# step 2 = Example = is question mai hame ek input lena padega or condtion check karni padegi .
# step 3 = psuedocode = 1.ek user variable lena padega input .
#                       2.if condtion check karni padegi if user = 0 print the number is zero
#                       3. elif Condition the user > 0 print the number is postive.
                        # 4. else condtion the number is negative.
                        # 5.show the answer
# step 4 = Translate =




print("=================QUESTION 1.==================")

user = int(input("Check The Number Is Positive, Negative or Zero : "))

if user == 0:
    print("The Number Is Zero")
elif user > 0:
    print("The Number Is Postive")
else:
    print("The Number Is Negative")

# step 5 = Dry Run(trace) = 
# step   user 
# 1       0             t
# 2      zero            f
#         5             t
# 3       postive         f
#           -6            t
# 4        neagtive       


print("===================QUESTION 2.================")
#2. Ek list of marks lo aur unka average nikalo.

# step 1 = restate = Ek list of marks lo aur unka average nikalo.
# step 2 = Example = Hum ek marks nam ka variable lege or us mai hum ek list create karenge.... 
# step 3 = psuedocode = 1. pehele hum ek varible lenge marks nam ka us mai hum ek list create karenge.
#                       2. or 2 variable to store the sum of the list.
#                       3. or 3 variable to store the total subject .
#                       4. then calculate the avarge (avg=sum/total subject)
#                       5.print the avrage.
# step 4 = Translate =

marks = [45,69,35,73,57]
sum_marks = sum(marks)
total_subject = len(marks)
avg = sum_marks/total_subject
print(f"Average is : {avg}")

# step 5 = Dry Run(trace) =
# step    marks             sum_marks       total_subject      avg
 
# 1     [45,69,35,73,57]

# 2     [45,69,35,73,57]     279

# 3    [45,69,35,73,57]       279            5

# 4      [45,69,35,73,57]       279          5               279/5=55.8

# 5     [45,69,35,73,57]       279         5                55.8


print("============QUESTION 3. ==========")

# 3. 1 se 20 tak ke numbers mein se sirf 3 ke multiples print karo.

# step 1 = restate = 1 se 20 tak ke numbers mein se sirf 3 ke multiples print karo output 3,6,9,12,15,18.
# step 2 = Example = direct hum for loop chalayenge or range (1,20) lenge.
# step 3 = psuedocode = 1. pehele hum for loop chalayenge 
#                       2. or us mai ham ye chalayenge if num % 3 the number is divisible by 3 then the print num
#                       3. then number is not divisible by 3 the print else part
#                      
#                       4.print the num.
# step 4 = Translate =
for num in range(1,20):
    if num % 3 == 0 :
        print(num)
    
# step 5 = Dry Run(trace) =
# Step          num      
# for 1         1
# if 1          1%3 f
# for 2         2
# if 2         2%3 f
# for 3        3
# if 3         3%3  t
#               3
# for 4         4 
# if 4          4%3 f
# for 5          5 
# if  5          5%3  f
# for 6           6
# if 6            6%3  t
#                  6
# for 7            7
# if 7             7%3  f
# for 8            8
# if 8             8%3   f
# for 9             9
# if 9             9%3     t
#                  9
# for 10             10
# if 10              10%3 f
# for 11             11
# if 11              11%3  f
# for 12             12
# if 12              12%3   t
#                     12
# for 13              13
# if 13               13%3 f
# for 14              f
# if 14                f
# for 15              15 
# if 15              15%3  t
#                      15
# for if 16           f
# for if 17          f
# for 18            18
# if 18             18%3   t
#                   18
# for if 19          f

# print(num)==3,6,9,12,18