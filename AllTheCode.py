class Author:
    def init(self, name):
        self.name = name


class Book:
    def init(self, isbn, title, author, counter):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.counter = counter

    def giveInfo(self):
        if self.isBorrowed == False:
            print(f"{self.title} by {self.author} - available")
        if self.isBorrowed == True:
            print(f"{self.title} by {self.author} - borrowed")


class Library:
    def init(self):
        self.shelf = [Book(isbn="1",
                           title="Quest Of The Sunfish - Escape To The Moon Islands",
                           author=Author("Mardi McConnochie"),
                           counter=20),
                      Book(isbn="2",
                           title="How To Survive On Mars",
                           author=Author("Jasmina Lazendic-Galloway"),
                           counter=3),
                      Book(isbn="3",
                           title="One Piece - Volume 1",
                           author=Author("Eiichiro Oda"),
                           counter=30),
                      Book(isbn="4",
                           title="Harry Potter and the Philosopher's Stone",
                           author=Author("J. K. Rowling"),
                           counter=1),
                      Book(isbn="5",
                           title="The Lord of the Rings",
                           author=Author("John Ronald Reuel Tolkien"),
                           counter=9)]

        self.bookByISBN = {book["isbn"]: book for book in self.shelf}

    def borrowBook(self, isbn):
        
        return self.bookByISBN.get(isbn)

    def displayBooks(self):
        print()
        for i in range(len(self.shelf)):
            userBook = self.shelf[i]
            print(f"{i + 1}.", end=" ")
            userBook.giveInfo()
        print()


myLibrary = Library()
print("Library menu:")
while True:
    userOption = input(
        " \nOption 1: Display the books.\n Option 2: Borrow a book.\n Option 3: Return a book.\n Option 4: Exit.\n Choose option(1-4):")

    if userOption == "1":
        myLibrary.dis2playBooks()

    if userOption == "2":
        myLibrary.displayBooks()
        userBook = int(input("Please enter the number for your book: "))
        bookchosen = myLibrary.shelf[userBook - 1]
        if bookchosen.isBorrowed == False:
            bookchosen.changeState(True)
            print(f"You have borrowed {bookchosen.title}.\n")
        else:
            print(f"{bookchosen.title} is already borrowed.")

    if userOption == "3":
        myLibrary.displayBooks()
        userBook = int(input("Please enter the number for your book: "))
        bookchosen = myLibrary.shelf[userBook - 1]
        if bookchosen.isBorrowed == True:
            bookchosen.changeState(False)
            print(f"You have returned {bookchosen.title}.\n")
        else:
            print(f"{bookchosen} is not borrowed.")

    if userOption == "4":
        print("\nClosing Library Menu...\n\n")
        exit()


        