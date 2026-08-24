# do Errors (ZeroDivisionError,ValueError)ko ek hi handaler se pakdo.

'''
1=restate=do Errors (ZeroDivisionError,ValueError)ko ek hi handaler se pakdo.
2=example=try:,except (ZeroDivisionError, ValueError) as e:,
3=psuedocode=1.try:,num = int(input("Number enter karo: ")),result = 100 / num,print("Result:", result)
             2.except (ZeroDivisionError, ValueError) as e:,print(f"Error : {e}")
4=trnsalte=

'''


try:
    num = int(input("Number enter karo: "))
    result = 100 / num
    print("Result:", result)

except (ZeroDivisionError, ValueError) as e:
    print(f"Error : {e}")

# 5=dry run