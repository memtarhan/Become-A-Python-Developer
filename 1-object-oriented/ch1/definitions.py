# A basic class
class Book:
    def __init__(self, title):
        self.title = title


book1 = Book(title="Animal Farm")
book2 = Book("Lord of the flies")

print(f"Book #1: {book1}")
print(f"Book #2: {book2.title}")
