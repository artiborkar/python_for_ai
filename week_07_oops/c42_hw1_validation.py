# BankAccount mein validation add karo taaki balance kabhi negative na ho.


class BankAccount:
    def __init__(self,balance):
        self._balance = balance
    

    def deposite(self,amount):
        if amount <= 0 :
            return print("Invalied Amount")

        if amount > self._balance:
            return print("Insufficent Balance")
        self._balance+=amount
        return print(f"Amount is {self._balance}")


    def withdrow(self,amount):
        if amount <= 0 :
            return print("Invalied Amount")

        if amount < self._balance:
            return print("Insufficent Balance")
        self._balance-=amount
        return print(f"Amount is {self._balance}")

    def get_balance(self):
        return print(self._balance)


bank_amount_obj = BankAccount(5200)

bank_amount_obj.get_balance()

bank_amount_obj.withdrow(-200)

# bank_amount_obj.deposite(2000)

# bank_amount_obj.deposite(-200)







# class BankAccount:
#     def __init__(self, balance):
#         if balance < 0:
#             print("Invalid initial balance")
#             self._balance = 0
#         else:
#             self._balance = balance

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Invalid amount")
#             return

#         self._balance += amount
#         print(f"Amount deposited. Current balance: {self._balance}")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Invalid amount")
#             return

#         if amount > self._balance:
#             print("Insufficient balance")
#             return

#         self._balance -= amount
#         print(f"Amount withdrawn. Current balance: {self._balance}")

#     def get_balance(self):
#         return self._balance


# bank_account_obj = BankAccount(5200)

# print(bank_account_obj.get_balance())

# bank_account_obj.withdraw(200)
# bank_account_obj.deposit(2000)

# bank_account_obj.deposit(-200)

# bank_account_obj.withdraw(10000)