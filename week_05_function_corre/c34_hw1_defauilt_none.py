# Homework
# add_to_list likho jo default None use kare, 3 alag baar call karke dikhao har baar fresh list aati hai.



def add_to_list(letter,lst= None):
    if lst is None:
        lst=[]
    lst.append(letter)

    return lst

print(add_to_list("Arti"))

print(add_to_list("Navneet"))

print(add_to_list("Vaishnav"))


