# Project 19 — Restaurant Bill (combine everything)
# EN: Write restaurant_bill(*prices, tax=5, tip=0) that returns the final total: sum of all item prices, plus tax%, plus tip%. Call it with tax defaulted and tip=10 passed as a keyword argument.
# हिंदी: restaurant_bill(*prices, tax=5, tip=0) बनाओ जो final total return करे: सभी item prices का जोड़, फिर tax%, फिर tip%। इसे एक बार tax को default रखते हुए और tip=10 keyword argument देकर call करो।
# Concepts: *args + keyword-only-style defaults together, percentage maths
# Hint: subtotal = sum(prices), then add subtotal * tax / 100 and subtotal * tip / 100.

print("====== Restaurant Bill=======")

def restaurant_bill(*prices, tax=5, tip=0):
    subtotal = sum(prices)
    print(subtotal)
    total_tax=subtotal * tax / 100
    print(total_tax)
    total_tip=subtotal * tip / 100
    print(total_tip)
    total=subtotal+total_tax+total_tip
    return total

final_total=restaurant_bill(2000,10,100)

print(f"Final Total is ={final_total}")