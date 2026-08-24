# Ek function set_marks(m) jo 0-100 ke bahar value par ValueError raise kare.


'''
1=restate=Ek function set_marks(m) jo 0-100 ke bahar value par ValueError raise kare
2=example=def set_marks(m):,print(set_marks(5))
3=spsuedocode=1.function is def set_marks(m):
              2.condition if m < 0 or m > 100:
              3.error handal karne ke liye raise ValueError("Your value is more than 100")
              4.return f"value is {m}"
              5.print the print(set_marks(5))'
              6.error ke liye print(set_marks(102))
4=translate=


'''
def set_marks(m):
    if m < 0 or m > 100:
        raise ValueError("Your value is more than 100")

    return f"value is {m}"

print(set_marks(5))

print(set_marks(102))


# 5=dry run=