# Ek abstract PaymentMethod with abstract pay(amount); Cash aur Card se implement karo.


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