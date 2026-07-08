print("=================password limit attempt program==========")

password = "python@123"
attemps = 0

while attemps < 3 :
    user_password = input ("enter the password : ")

    if user_password == password :
        print("logged in successfully")
        break
    else:
        print("please enter correct password.")
    attemps += 1

if attemps ==3 :
    print("Account locked")