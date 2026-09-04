# Ek @dataclass Book banao (title, author, year) aur 2 objects compare karo.


'''
1=restate= Ek @dataclass Book banao (title, author, year) aur 2 objects compare karo.
2=example= from dataclasses import dataclass , @dataclass 
3=psuedocode= 1.from dataclasses import dataclass
              2. decorator @dataclass 
              3.create the class class Book
              4.parameter title : str ,  author : str , year : int|float
              5.object is  book = Book("Python" , "Guido van" , 1991) 
              6.and print(book)
              7.compair book2 = book == book1
              8.print(book2)
4=translate in python=
'''


from dataclasses import dataclass

@dataclass 

class Book:
    title : str
    author : str
    year : int|float

book = Book("Python" , "Guido van" , 1991)
book1 = Book("Python" , "Guido van" , 1991)

print(book)

book2 = book == book1

print(book2)


# dryrun =
