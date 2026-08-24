# Ek BankAccount class (Week 7) mein withdraw ko 
# custom InsufficientFundsError raise karwao.


class InsufficientFundsError(Exception):
    """ Raise the  insufficient fund error """
    pass

class BankAccount():
    def __init__(self,balance):
        self.balance = balance


    def withdraw(self,amount):
        if self.balance < amount:
            raise InsufficientFundsError("your amount is more than blance")
        else:
            self.balance -= amount
            print("sucessful" )

ba = BankAccount(500)

ba.withdraw(200)

ba.withdraw(1000)