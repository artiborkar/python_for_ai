# ek program jo list se index access kare ,  ValueError aur IndexError dono alag handle kare.


'''
1=restate=ek program jo list se index access kare ,  ValueError aur IndexError dono alag handle kare.
2=example=numbers = [10, 20, 30, 40, 50],try:except (ValueError ,IndexError )as e:
3=psuedocode=1.write lst numbers = [10, 20, 30, 40, 50]
             2.try:,index = int(input("Index enter karo: ")),print("Value:", numbers[index])
             3.except (ValueError ,IndexError )as e:,print(f"Error :{e}")

4=transalte=
5=dry run =

'''

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter The Index No.  : "))
    print("Value:", numbers[index])

except (ValueError ,IndexError )as e:
    print(f"Error :{e}")




