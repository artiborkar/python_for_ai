# Cart class mein __len__ add karo jo items ki sankhya de.

# 1=restate= Cart class mein __len__ add karo jo items ki sankhya de.
# 2=example=class Cart:, def __len_
# 3=psuedocode=1.class Cart :,method def__init(self),self.items=[]
             # 2.2nd method def add(self,word)
            #  3.self.items.append(word)
             # 4.3rd method is def __len__(self)
            # 4. return len(self.items)
# 4=translate python =

print("--------Homework 2------")

class Cart:

    def __init__(self):

        self.items=[]

    def add (self,word):

        self.items.append(word)

    def __len__(self):

        return len(self.items)

    
cart = Cart()

cart.add("arti")

cart.add("Rohini")

cart.add("Navneet")

print(len(cart))



# 5=dry run =
# cart = Cart()
# def __init__(self):

#         self.items=[]
# cart.add("arti")
# def add (self,word):

#         self.items.append(word)

# print(len(cart))
# def __len__(self):

#         return len(self.items)





