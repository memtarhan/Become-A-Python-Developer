class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


b1 = Book(title="The Catcher In The Rye")
b2 = Book(title="The Grapes of Wrath")
n1 = Newspaper(name="The Washington Post")
n2 = Newspaper(name="The New York Times")


# use type() to inspect the object type
print(type(b1))
print(type(n1))

# compare two types together
print(type(b1) == type(b2))
print(type(b1) == type(n1))

# use isinstance 
print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))


