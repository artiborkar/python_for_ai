# Temperature class mein staticmethod c_to_f(c) add karo.


# 1=restate=# Temperature class mein staticmethod c_to_f(c) add karo.
# 2=example=class Temperature:,@staticmethod
# 3=psuedocode=1.write  class Tempreature  decorator @staticmethod
#              2.method def  c_to_f(c): ,  return c * 9 / 5 + 32
#              3.print the method print(temp.c_to_f(20))
# 4=translate python =


print("-------homework 2----------")
class Temperature:
    @staticmethod
    def  c_to_f(c):
        return c * 9 / 5 + 32


temp=Temperature()

print(temp.c_to_f(20))

# 5=dry run=

# print(temp.c_to_f(20))
# class Temperature:
#     @staticmethod
#     def  c_to_f(c):
#         return c * 9 / 5 + 32
