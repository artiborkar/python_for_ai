# Ek function jo int | None return kare (mile toh number, nahi toh None).


'''
1=restate= Ek function jo int | None return kare (mile toh number, nahi toh None).
2=example= def my_fun(n)->int | None , print(my_fun(23)),print(my_fun("arti"))
3=psuedocode= 1.create function  def my_fun(n)->int | None
              2.check the condtion the parameter is intiger or none if isinstance(n,int)
              3.return f"Number is : {n}"
              4.else:,return f"None "
              5.print print(my_fun(23)) ,print(my_fun("arti"))
4=transalte=

'''
def my_fun(n)->int | None:
    if isinstance(n,int) :
        return f"Number is : {n}"

    else:
        return f"None "

print(my_fun(23))

print(my_fun("arti"))


# dry run 
# print(my_fun(23))
# def my_fun(n)->int | None
# if isinstance(n,int)
# return f"Number is : {n}"
# print(my_fun("arti"))
# def my_fun(n)->int | None
# if isinstance(n,int) :
#   else:
# return f"None "