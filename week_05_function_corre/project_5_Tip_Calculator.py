# Project 5 — Tip Calculator
# EN: Write a function tip_amount(bill, percent) that returns how much tip to pay. Then print the total bill (bill + tip) for a ₹800 bill at 10%.
# हिंदी: एक function tip_amount(bill, percent) बनाओ जो tip की रकम return करे। फिर ₹800 के bill पर 10% tip के साथ कुल bill (bill + tip) print करो।
# Concepts: return, using the returned value in more maths
# Hint: return bill * percent / 100, then total = bill + tip_amount(800, 10).

print("======Tip Calculator=====")

def tip_amount(bill, percent):

    return bill * percent / 100

    print(f"Total = {bill}+tip_amount(800,10)")

print(tip_amount(30,3))


# def tip_amount(bill, percent):
#     return bill * percent / 100

# tip = tip_amount(800, 10)
# total = 800 + tip

# print("Tip:", tip)
# print("Total Bill:", total)                    #not clear