
# recursion se factorial (6)nikaalo.

def factorial(x):

    print(x)

    if x==1:

        return 1 

    return x*factorial(x-1)

    
print(factorial(6))




