# ek @count_calls decorator jo gine function kitni baar call hua.

'''
1=restate= ek @count_calls decorator jo gine function kitni baar call hua.
2=example= def count_calls(func): , @count_calls
3=psuedocode= 1.def count_calls(func)
              2.craete variable count is 0 , 2nd func is def wrapper()
              3.call the variable nonlocal count, result = func(),count += 1
              4.retuen 1st func return  result ,  2nd func return wrapper
              5.call the decorator @count_calls
              6.new var is def info() ,return "I am a Agentic AI engineer"
              7.print(info())

4=translate=

'''

def count_calls(func):
    count = 0
    def wrapper():
        nonlocal count
        result = func()
        count += 1
        
        print(f"The Function {count} Times")
        return  result


    return wrapper



@count_calls
def info():
    return "I am a Agentic AI engineer"

print(info())

print(info())

print(info())