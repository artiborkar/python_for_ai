
# @timer ko ek function par lagao jo loop chalata hai.


'''
1=restate= @timer ko ek function par lagao jo loop chalata hai.
2=example=  import time, def timer(func), @timer 
3=psudocode= 1.import time
            2.function def timer(func) ,2nd function def wrapper() ,star time is time.time() function
            3.store the decorator is result  = func() and end time is end_time = time.time()
            4.return the outer function  return result inner function  return wrapper
            5.decorator @timer
            6. check condition for i in range(6):, and print variable print(i)
            7.print the function print(timing())
4=translate in python =



'''
import time

def timer(func):
    def wrapper():
        start_time = time.time()
        result  = func()
        end_time = time.time()
        print(f"time Taken {(end_time - start_time)} second")

        return result
    return wrapper

@timer 

def timing():
    for i in range(6):
        print(i)
    return "you are very Lacky your timig is perfect"

print(timing())