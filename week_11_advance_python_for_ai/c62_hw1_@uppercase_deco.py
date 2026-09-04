# EK @uppercase decorator banao jo function ke string-result ko uppercase kare.

'''
1=restate=  EK @uppercase decorator banao jo function ke string-result ko uppercase kare.
2=example= def upeercase(func) , @ upeercase
3=psuedocode= 1.fnction is def upeercase(func) 2nd function def wrapper()
              2.call the 1st function result = func() , return result.upper()
              3. return wrapper
              4. @ upeercase  , def info() , return "I am Agentic AI engineer"
              5. print(info())
4=transalte in python=

'''


def upeercase(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


@ upeercase
def info():
    return "I am Agentic AI engineer"


print(info())

# dry run 
# 
# def info()
# def upeercase(func)
# def wrapper()
# result = func()
# return result.upper()
# return "I am Agentic AI engineer"
# print(info())