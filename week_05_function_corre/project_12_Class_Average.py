# Project 12 — Class Average (*args with a guard)
# EN: Write average(*marks) that returns the average of any number of marks. If called with no marks, return 0 (avoid divide-by-zero).
# हिंदी: average(*marks) बनाओ जो कितने भी marks का average return करे। अगर बिना marks के call हो तो 0 return करो (divide-by-zero से बचो)।
# Concepts: *args, len(), guard condition
# Hint: if len(marks) == 0: return 0 first, then return sum(marks) / len(marks).

'''
restate1=I am calculate the avrage of the multiple number .
example2=given function name is average(*marks) argument is a *marks 
pusedocode3=1.create the fun name is average  our parameter is (*marks)
            2.then check the if statement is marks==0 this condtion is true then the return 0
            3.clculate the sum is sum(marks) and print 
            4.calculate the length of tuple len_marks and print
            5.if marks==0 is flase then the return f"Avrage is {sum_marks / len_marks}"
            4.print the function name with parameter.
translate4=
dryrun5=
average(*marks)
average(45,67,89,32)
if len(marks)==0 ff
sum_marks=sum(marks):233
len_marks=len(marks):4
 return f"Avrage is {sum_marks / len_marks}"
 print(average(45,67,89,32))
 ouput is Avrage is 58.25

'''

print("========Class Average (*args with a guard)======")

def average(*marks):

    if len(marks)==0:
        
        return 0 
    sum_marks=sum(marks)
    print(f"sum of the item:{sum_marks}")
    len_marks=len(marks)
    print(f"Length of list:{len_marks}")
    return f"Avrage is {sum_marks / len_marks}"



print(average(45,67,89,32))