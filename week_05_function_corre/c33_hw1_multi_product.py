# Homework
# multiply_all(*nums) jo saare numbers ka product return kare.




def multiply_all(*nums):

    product = 1 

    for num in nums:

        product*=num

    return product
    
print(multiply_all(2,3))