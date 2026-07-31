
# Number guessing game ke 'compare' part ko ek function check_guess(guess, secret) mein nikaalo jo "low"/"high"/"correct" return kare.

# step 1= restate = Number guessing game ke 'compare' part ko ek function check_guess(guess, secret) mein nikaalo jo "low"/"high"/"correct" return kare.
# step 2 =example = guess == secret:return "Correct", elif guess > secret:return "Too High",return "Too Low"
# step 3 = psuedocode = 1.crete a function , function name is check_guess(guess, secret).
                        # 2.  check the satement if is  if guess == secret: Correct    elif guess > secret:Too High  else: return "Too Low
                        # 3 . call the function name and the argument
                        # 4. print result

# step 4=translate

def check_guess(guess, secret):
    if guess == secret:
        return "Correct"
    elif guess > secret:
        return "Too High"
    else:
        return "Too Low"

print(check_guess( 42 , 42))

print(check_guess( 60 , 42))

print(check_guess( 30 , 42))

# step 5 = dry run 
# def check_guess(guess, secret):
# if guess == secret:# print(check_guess( 42 , 42))
        # return "Correct"
# def check_guess(guess, secret):
# elif guess > secret:print(check_guess( 60 , 42))
        # return "Too High"
# else:print(check_guess( 30 , 42))
        # return "Too Low"