class Book:
    # Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # double-underscore properties are hidden from other classes
    __book_list = None

    # create a class method
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    # create a static method
    @staticmethod
    def get_book_list():
        if Book.__book_list is None:
            Book.__book_list = []
        return Book.__book_list

    def __init__(self, title, book_type):
        self.title = title
        if book_type in Book.BOOK_TYPES:
            raise ValueError("Book type is not valid")
        else:
            self.book_type = book_type

    def set_title(self, title):
        self.title = title


print(f"Book types: {Book.get_book_types()}")

b1 = Book(title="The Catcher In The Rye", book_type="EBOOK")
books = Book.get_book_list()
books.append(b1)
print(books)

