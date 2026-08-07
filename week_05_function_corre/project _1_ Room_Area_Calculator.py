# Project 1 — Room Area Calculator
# EN: Write a function room_area(length, width) that returns the area of a room. 
# Use it to find the area of 3 different rooms and print each result.
# हिंदी: एक function room_area(length, width) बनाओ जो कमरे का area return करे। 
# इसे 3 अलग-अलग कमरों का area निकालने के लिए इस्तेमाल करो और हर result print करो।
# Concepts: def, two parameters, return, function call
# Hint: return length * width. Print the call: print(room_area(10, 12)).

'''
step 1= restate =Write a function room_area(length, width) that returns the area of a room. 
step 2= example =length * width , room_area(10, 12)
step 3 = psuedocode = 1 create the function  room_area(length, width): is given.
                      2  return the length * width
                      3 print and call the function

step 4 =translate=
'''
print("===== Project 1 — Room Area Calculator=====")

def room_area(length, width):

    return length * width

print(room_area(10, 12))

print(room_area(12, 12))

print(room_area(20, 10))

# step 5 dry run
# def room_area(length, width):
#  return length * width
# print(room_area(10, 12))
# output 120