# safe division : do number lo , division karo , ZeroDivisionError Handal karo.

'''
1=restate=safe division : do number lo , division karo , ZeroDivisionError Handal karo.
2=example=try:,except ZeroDivisionError as e:,else:
3=psuedocode=1.try:num1 = int(input("Enter The First Number:"))num2 = int(input("Enter The Second Number:"))
             2.result = num1 / num2,print(result)
             3.except ZeroDivisionError as e:
             4.print(f"Error : {e}"),print("does not any number divied by zero"),print("Please Enter the vallied number")
             5.else:, print("well done your number is valied")
4=transalte


'''

try:
    num1 = int(input("Enter The First Number:"))
    num2 = int(input("Enter The Second Number:"))
    result = num1 / num2
    print(result)

except ZeroDivisionError as e:
    print(f"Error : {e}")
    print("does not any number divied by zero")
    print("Please Enter the vallied number")

else:
    print("well done your number is valied")


# 5=dry run =
