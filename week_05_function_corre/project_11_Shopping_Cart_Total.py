# Project 11 — Shopping Cart Total (*args)
# EN: Write cart_total(*prices) that returns the sum of any number of item prices. Test it with 3 prices and with 6 prices.
# हिंदी: cart_total(*prices) बनाओ जो कितने भी item prices का जोड़ return करे। इसे 3 prices और 6 prices के साथ test करो।
# Concepts: *args, sum()
# Hint: return sum(prices). Inside, prices is a tuple.

'''
resate1=I want the sum of *prices and print the sum
example2=that is my funcation name is cart_total and return the sum of price and print the sum
psuedocode3=1.create the function with function name and parameter
            2.return the sum of parameter 
            3.print the function name with multiple arguments
translate4=
dry run 5=
cart_total(*price)
(223,46,78)
sum(price)
print(cart_total(223,46,78))
output is 347
'''


print("=======Shopping Cart Total (*args)=====")

def cart_total(*price):

    return sum(price)

print(cart_total(223,46,78))