# Money class (amount) mein __eq__ add karo taaki same amount equal ho.

# 1=restate=Money class (amount) mein __eq__ add karo taaki same amount equal ho.
# 2=Example=class Money,def __init__(self,amount),def__eq__(self,data)
# 3=psuedocode=1.write class Money : method def __init__(self,amount)
            #  2.self.amount=amount
            #  3.def __eq__(self,data) method
            #  4.return the self.amount==data.amount
            #  5.create the object m1=Money(200)
            #  2nd object is m2=Money(300)

# 4=translate=

print("-------homework1----------")

class Money:
    def __init__(self,amount):
        self.amount=amount

    def __eq__(self,data):
        return self.amount == data.amount

m1=Money(200)

m2=Money(300)

m3=Money(300)

m=m1==m2

m4=m2==m3

print(m)

print(m4)


# 5=dry run=


# 1.m=m1==m2
# 2. def __init__(self,amount):
#         self.amount=amount

# 3.print(m4)
# 4.def __eq__(self,data):
#         return self.amount == data.amount