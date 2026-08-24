# int(input) mein ek try with ValueError aur ek genral Exception fallback.

'''
1=restate=int(input) mein ek try with ValueError aur ek genral Exception fallback.
2=example=try:,except ValueError as e:,except Exception as e:
3=psuedocode=1.try:,num = int(input("Number enter karo: ")),print("Number:", num)
             2.except ValueError as e:,print(f"Error {e}")
             3.except Exception as e:,print(f"Error {e}"),print("Error")
4=transalte=


'''


try:
    num = int(input("Number enter karo: "))
    print("Number:", num)

except ValueError as e:
    print(f"Error {e}")

except Exception as e:
    print(f"Error {e}")
    print("Error")


# 5=dry run