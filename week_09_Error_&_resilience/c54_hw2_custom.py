# Ek custom exception NegativeNumberError banao aur ek function jo negative par use raise kare.


# 1=restate=Ek custom exception NegativeNumberError banao aur ek function jo negative par use raise kare.
# 2=example=class NegativeNumberError(Exception):,def negative(num):,negative(-65)
# 3=psuedocode=1.class NegativeNumberError(Exception):, pass
#              2.function create def negative(num):
#              3.condition if num < 0:,raise NegativeNumberError("The Number are negative More than the zero(0)"
#              4.elif num > 0 :, print(f"Postive Number:{num}")
#              5. else:, print(f"Zero Number: {num}")
#              6.call the function negative(-65)
# 4=transalte=



class NegativeNumberError(Exception):
    "raise the negative number error "
    pass

def negative(num):
    if num < 0:
        raise NegativeNumberError("The Number are negative More than the zero(0)")
        
    elif num > 0 :
        print(f"Postive Number:{num}")

    else:
        print(f"Zero Number: {num}")

negative(0)

negative(55)

negative(-65)


# 5=dry run=