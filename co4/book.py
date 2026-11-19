class Publisher:  # Parent class
    def __init__(self, name):
        # Constructor to initialize publisher name
        self.name = name

    def display(self):
        # Method to display publisher name
        print("Publisher Name:", self.name)


class Book(Publisher):  # Book class inherits Publisher class
    def __init__(self, name, title, author):
        # Constructor to initialize book details
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        # Override display() method of Publisher class
        super().display()
        print("Title:", self.title)
        print("Author:", self.author)


class Python(Book):  # Python class inherits Book class
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):
        # Override display() method of Book class
        super().display()
        print("Price: Rs.", self.price)
        print("Number of Pages:", self.no_of_pages)


# Get book details from the user
publisher_name = input("Enter the publisher's name: ")
book_title = input("Enter the book's title: ")
book_author = input("Enter the book's author: ")
book_price = float(input("Enter the price of the book: "))
book_pages = int(input("Enter the number of pages: "))

# Create an object of Python class
bk = Python(
    publisher_name,
    book_title,
    book_author,
    book_price,
    book_pages
)

print("\n--- Book Details ---")
bk.display()
