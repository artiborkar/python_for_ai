# Apna context manager @contextmanager se banao jo "Enter"/"Exit" print kare.


'''
1=restate= Apna context manager @contextmanager se banao jo "Enter"/"Exit" print kare.
2=example=  from contextlib import contextmanager , @contextmanager
3=psuedocode= 1 .from contextlib import contextmanager
              2. @contextmanager 
              3. def my_func(func)->str: , print("Enter") ,  yield ,print("Exit")
              4.with my_func("my decorator"):  , print("inside")
4=transalte=

'''


from contextlib import contextmanager


@contextmanager

def my_func(func)->str:
    print("Enter")
    yield
    print("Exit")

with my_func("my decorator"):
    print("inside")


# 5=dry run =
# with my_func("my decorator"):
# def my_func(func)->str:
# # print("Enter")....Enter
# print("inside")......inside
# print("Exit").......Exit

