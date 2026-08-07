# recursion se 5 se 1 tak countdown karo.

def countdown(n):

    print(n)

    if n == 1:

        return 
    
    countdown(n-1)

countdown(5)