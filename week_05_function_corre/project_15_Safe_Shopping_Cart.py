# Project 15 — Safe Shopping Cart (mutable-default trap)
# EN: Write add_item(item, cart=None) correctly so that each fresh call (without a cart) starts with an EMPTY cart. Call it 3 separate times and show each returns only its own item. (Do NOT use cart=[] — explain in a comment why.)
# हिंदी: add_item(item, cart=None) सही तरीके से बनाओ ताकि हर नई call (बिना cart के) खाली cart से शुरू हो। इसे 3 अलग बार call करके दिखाओ कि हर बार सिर्फ़ अपना item आता है। (cart=[] मत इस्तेमाल करो — comment में कारण लिखो।)
# Concepts: mutable default trap, None sentinel, is None
# Hint: if cart is None: cart = [] — this makes a fresh list every call.


'''
restate1=the question is the to call the any  item in any of the time then the list is create in new
exampe2=['Arti']['Shreya']['Rohini'] not include in single list
psuedocode3=1.create the function with function name is add_item and parameter is item, cart=None
            2.check the is cart is None if true then the cart=[] add 
            3.then the cart.append (item)
            4.return the cart
            5.print the funcation name with argument
translate4=
dry run5=
def add_item(item, cart=None)
if cart is None
 cart=[]
cart.append(item)
print(add_item("Arti"))
return cart
output is ['Arti']
'''
print("======Safe Shopping Cart=====")

def add_item(item, cart=None):#---->cart=[] hum isiliye use nhi krt because the hum jo agrument dete hai vo ek hi list mai dete hai .

    if cart is None:
        cart=[]
    cart.append(item)
    return cart
    # print(cart)

print(add_item("Arti"))

print(add_item("Shreya"))

print(add_item("Rohini"))

