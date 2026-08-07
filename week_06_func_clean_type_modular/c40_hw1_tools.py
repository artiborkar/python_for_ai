# tools.py mein ek aur function add karo: is_palindrome(text: str) -> bool (typed + docstring).

'''
1=restate= create  the palindrome code
2=example=  any text to check the palindrom or not like "arti"is palindrom not 
3=psuedocode= create the function name is_palindrome
             parameter is (text: str) 
             return output is  bool type
             check the text == text[::-1]
             this condtion is true then return true
             condtion is false then the return is false
             call the function 
             print

4=translate
5=dry run = 
is_palindrome(text: str) -> bool 
if text==text[::-1]:
is_palindrome("Arti")
else:
        return False
is_palindrome("nayan")
 return True


'''
def is_palindrome(text: str) -> bool :
    '''
    function:
        is_palindrome:
            parameter: is text and return in str or
            output : is bool value

    return :
             text==text[::-1]


    '''

    if text==text[::-1]:
        return True
    else:
        return False

print(is_palindrome("Arti"))
print(is_palindrome("nayan"))