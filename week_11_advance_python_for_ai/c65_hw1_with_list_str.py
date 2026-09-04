# Ek function likho with list[str] parameter aur dict[str, int] return type.

'''
1=restate=  Ek function likho with list[str] parameter aur dict[str, int] return type.
2=example= ef my_list_dict(name : list[str])->dict[str,int]
3=psuedocode= 1.crete a function with type hint def my_list_dict(name : list[str])->dict[str,int]:
              2.return {"Arti":21,"Naneet":13}
              3.print function name
4=

'''
def my_list_dict(name : list[str])->dict[str,int]:
    return {"Arti":21,"Naneet":13}


print(my_list_dict(["Arti","Navneet","Pooja"]))


# dry run
# print(my_list_dict(["Arti","Navneet","Pooja"]))
# def my_list_dict(name : list[str])->dict[str,int]:
    # return {"Arti":21,"Naneet":13}
    # {'Arti': 21, 'Naneet': 13}  output