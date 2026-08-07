# make_adder(n) closure banao jo  n add kare; make_adder(5) test kro.


def make_adder(n):

    print("value of n:",n )

    def my_var(m):

        print("value of m:",m)

        return n+m

    return my_var

result=make_adder(5)

print(result)

print(result(3))

