# 3 objects ki list banao aur print karke dekho __repr__ kaise kaam karta hai.


# 1=restate= 3 objects ki list banao aur print karke dekho __repr__ kaise kaam karta hai.
# 2=Example=humne direct import kiya hai Book class ke
# 3=psuedocode=1.from c46_hw2__repr__ import Book
#              2.3 object create book1,book,2,book3,
#              3.book nam ke list mai store kiye,book = [book1,book2,book3]
#              4.print(book)
#              5.but ye c46_hw2__repr__ yaha se check hokar ayega or pura line exexute hone ke bad ye print hoga.


# 4=transalte python=

print("--------homework3--------------")

from c46_hw2__repr__ import Book

book1 = Book("python","Guido van Rossum") 

book2=Book("agentic ai","Guido Van rossum")

book3=Book("c","Dennis Ritchie")

book = [book1,book2,book3]

# print(repr(book))

print(book)

# 5.dry run=
