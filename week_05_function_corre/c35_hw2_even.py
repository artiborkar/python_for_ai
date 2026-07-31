# Ek function is_even(n) jo True/False return kare; 5 numbers par test karo.

# step 1 = restate = find the given number is true or false
# step 2 = example = print(is_even(5)) this number is false
# step 3 = psuedocode = 1 . create the function is is_even(n) function name is given
                        # 2 . then check the number is % 2==0
                        # 3 .the number is divsiable then the number is true
                        # 4. not divisiable then no.is false.
                        # 5 . call the function 
                        # 6. print ans

# step 4 translate python code:
def is_even(n) :
    if n % 2 == 0 :
        return True
    else:
        return False

print(is_even(5))

print(is_even(20))

print(is_even(150))

print(is_even(177))

# step 5 =dry run
# print(is_even(5))
# def is_even(n) :
# if 5 % 2 == 0 :   flase
# return False