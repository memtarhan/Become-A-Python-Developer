# A basic class
class Book:
    # the 'init' function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret"

    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount) / 100
        return self.price

    def set_discount(self, amount):
        self._discount = amount


book = Book(title="Animal Farm", author="George Orwell", pages=84, price=13.10)

# print(f"Book: {book}")
# print(f"Book's title: {book.title}")
# print(f"Book's regular price: {book.get_price()}")
# book.set_discount(10)
# print(f"Book's on-sale price: {book.get_price()}")

print(book.__secret)