# Project 7 — Discount Price Calculator
# EN: Write a function final_price(price, discount_percent) that returns the price after discount. Print the final price of a ₹1500 item with 20% off.
# हिंदी: एक function final_price(price, discount_percent) बनाओ जो discount के बाद की कीमत return करे। ₹1500 के item पर 20% छूट के बाद final price print करो।
# Concepts: return, percentage maths
# Hint: return price - (price * discount_percent / 100).


'''
restate1=Write a function final_price(price, discount_percent) that returns the price after discount. Print the final price of a ₹1500 item with 20% off.
example2= return price - (price * discount_percent / 100) is given and return 1200.
psuedocode3=1:create a functuion def final_price(price, discount_percent):
            2:return the return price - (price * discount_percent / 100)
            3. print (final_price(1500,20))
translate4=
dry run5=
final_price(price, discount_percent)
(1500,20)
 price - (price * discount_percent / 100)
 output 1200
'''


print("======Discount Price Calculator======")

def final_price(price, discount_percent):

    return price - (price * discount_percent / 100)

print(final_price(1500,20))