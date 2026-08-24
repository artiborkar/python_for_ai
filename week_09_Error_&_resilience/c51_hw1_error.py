# jann boojh kar 3 alag  error banano.(ZeroDivisionError , ValueError , IndexError) aur traceback padho.

'''
1 = restate =jann boojh kar 3 alag  error banano.(ZeroDivisionError , ValueError , IndexError) aur traceback padho.
2=example=ZeroDivisionError,IndexError,ValueError
3=psuedocode=1.def div(x,y):,print(x/y), div(10,0)
             2. lst = [10,20,30,40], print(lst[4])
             3.def err(a):,if a < 0 :, raise ValueError("less than zero is not allow"),err(-1)

4=translate to python =


'''
print("------------ZeroDivisionError------------")

# def div(x,y)

#     print(x/y)

# div(10,0)


print("-----------IndexError-------------")

# lst = [10,20,30,40]

# print(lst[4])


print("-----------ValueError -------------")

def err(a):
    if a < 0 :
        raise ValueError("less than zero is not allow")

err(-1)