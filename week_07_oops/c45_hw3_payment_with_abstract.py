# Ek abstract PaymentMethod with abstract pay(amount); Cash aur Card se implement karo.

# 1=restate= Ek abstract PaymentMethod with abstract pay(amount); Cash aur Card se implement karo.
# 2=example=import the abc file .and create 1 parent class PaymentMethod and 2 child method.
# 3=psuedocode=1.from abc import ABC , abstractmethod
#              2.then parent class PaymentMethod 
# 5=transalte
# 6=dry run 

print("--------HOMEWORK------------")

from abc import ABC , abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        ...


class Cash(PaymentMethod):
    def pay(self,amount):
        return f"cash on Payment {amount}"

class Card(PaymentMethod):
    def pay(self,amount):
        return f"card on payment {amount}"

print(Cash().pay(400))

print(Card().pay(100))