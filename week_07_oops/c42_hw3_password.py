# Ek Password class with _password aur ek check(guess) method jo True/False de.

class Password:
    def __init__(self,password):
        self._password = password

    def check(self,guess):
        return self._password == guess
        
        # if self._password == guess:
        #     return True
        # else:
        #     return False


pass_obj = Password("arti@123")

print(pass_obj.check("arti"))

print(pass_obj.check("arti@123"))


