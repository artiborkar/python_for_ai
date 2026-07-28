
# Live demo — FizzBuzz (5-step method ke saath)

# step 1:restate = there are three condition and three step in program aur output fizz,buzz,fizzbuzz.
# step 2:Exaple = first condition is num%3==0 and num%5==0 2nd num%3==0 3rd num %5==0.
# step 3:psuedocode = 1.start the for loop range 1,20
#                     2. if statement the check the condtion num%3==0 and num%5==0 is true then print fizzbuzz.
#                     3. condtion is false then 2nd statement is elif check num%3==0 is true then print fizz.
#                     4. this condtion is flase then the 2nd condtion is 2nd elif num%5==0 print buzz
#                     5. or thino condtion false then else is execute then print number
# step 6:Translate=
for num in range(1,20):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num) 


 