# ek try / except / else/ finally ka poora likho jo chaaron block dikhaye.

'''
1=restate= ek try / except / else/ finally ka poora likho jo chaaron block dikhaye.
2=example=try / except / else/ finally 
3=psuedocode=1.try:,num = int(input("Number enter karo: ")),result = 100 / num
             2.except (ZeroDivisionError ,ValueError) as e:,print(f"Error: {e}")
             3.else:,print("Result:", result)
             4.finally:,print("Program finished")
4=translate=

'''
try:
    num = int(input("Number  the enter : "))
    result = 100 / num

except (ZeroDivisionError ,ValueError) as e:
     print(f"Error: {e}")

else:
    print("Result:", result)

finally:
    print("Program finished")




# 5=dry run=
# num = int(input("Number  the enter : ")):5

#     result = 100 / 5
# else:
#     print("Result:", result)

# finally:
#     print("Program finished")


