# Project 30 — Shopping Cart & Invoice Generator (capstone)
# EN: Build a shopping system. Functions: add_item(cart, name, price, qty) (returns updated cart list of dicts), cart_subtotal(cart), 
# apply_discount(subtotal, percent=0), and print_invoice(cart, discount_percent=0). Add at least 3 items, apply a discount, 
# and print a neat itemised invoice with subtotal, discount, and grand total.
# हिंदी: एक shopping system बनाओ। Functions: add_item(cart, name, price, qty) (dicts की updated cart list return करे), cart_subtotal(cart),
#  apply_discount(subtotal, percent=0), और print_invoice(cart, discount_percent=0)। कम से कम 3 items जोड़ो, discount लगाओ, 
# और subtotal, discount, और grand total के साथ साफ़-सुथरा itemised invoice print करो।
# Concepts: list of dicts, multiple cooperating functions, defaults, return, formatting
# Hint: Each cart item is a dict {"name":..., "price":..., "qty":...}. Subtotal = sum(i["price"] * i["qty"] for i in cart).

print("-----------Shopping Cart & Invoice Generator---------")


def add_item(cart,name,price,qty):

    lst_of_items = {
                    "name"=name,
                    "price"=price,
                    "qty"=qty
                  }

    cart.append(lst_of_items)
    return cart


def cart_subtotal(cart):
    
    subtotal = 0

    for item in cart:
        subtotal+=item["price"]*item["qty"]

        return subtotal

def apply_discount(subtotal,percent=0):
    
    discount = subtotal*percent/100

    



# def print_invoice(cart,discount=0):
