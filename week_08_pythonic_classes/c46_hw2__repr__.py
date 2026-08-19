# Book class (title, author) mein __repr__ add karo.


# 1=restate=Book class (title, author) mein __repr__ add karo.
# 2=example=class Book:,def __init__(title,author),def __repr__.
# 3=psuedocode=1,Write the class Book:
                # 2.special method def __init__(self,title,author):
                # 3.self.title=title,self.author=author.
                # 4.2nd special method is __repr__(self)
                # 5.return f"Book(title{self.title}author{self.author})"
                # 6.crete the object ,print(repr(object_name))
# 4=translate=


print("---------homework2---------------")


class Book:

    def __init__(self,title,author):
        self.title=title
        self.author=author

    def __repr__(self):
        return f"Book(title = {self.title} , author = {self.author})"


book1 = Book("python","Guido van Rossum")

print(repr(book1))


# 5=dry run=
# 1.book = Book("python","Guido van Rossum")
# 2.def __init__(self,title,author):
        # self.title=title
        # self.author=author
# 3.print(repr(book))
# 4. def __repr__(self):
        # return f"Book(title = {self.title} , author = {self.author})"
