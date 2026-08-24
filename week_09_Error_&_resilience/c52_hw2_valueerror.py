# safe int conversion: user input ko int banao , ValueError handal krke "Invalied bolo".

'''
1=restate=safe int conversion: user input ko int banao , ValueError handal krke "Invalied bolo".
2=example=try:,except ValueError as e:
3=psuedocode=1.try:,num = int(input("Number enter karo: ")),print("Number:", num)
             2.except ValueError as e:,print("Invalied ")
4=transalte=

'''

try:
    num = int(input("Number enter karo: "))
    print("Number:", num)

except ValueError as e:
    print("Invalied ")


# 5=dry run
# try:
#     num = int(input("Number enter karo: ")):arti
# except ValueError as e:
#     print("Invalied ")
#     print("Number:", num)