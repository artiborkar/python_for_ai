print("=============== Username Limit Attempt Program ===============")

username = "artiborkar"
attempts = 0

while attempts < 3:
    user_username = input("Enter the username: ")

    if user_username == username:
        print("Logged in successfully")
        break
    else:
        print("Please enter the correct username.")
        attempts += 1

if attempts == 3:
    print("Account locked")