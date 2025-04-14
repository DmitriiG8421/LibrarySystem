import sqlite3

connection = sqlite3.connect("booksDataBase.db")
connection.row_factory = sqlite3.Row

class Author:
    def __init__(self, name):
        self.name = name


class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.isBorrowed = False

    def giveInfo(self):
        if self.isBorrowed == False:
            print(f"{self.title} by {self.author.name} - available")
        if self.isBorrowed == True:
            print(f"{self.title} by {self.author.name} - borrowed")

    def changeState(self, state):
        self.isBorrowed = state




class Library:
    def __init__(self):

        self.books = [Book("Quest Of The Sunfish - Escape To The Moon Islands", Author("Mardi McConnochie")),
                      Book("How To Survive On Mars", Author("Jasmina Lazendic-Galloway")),
                      Book("One Piece - Volume 1",Author("Eiichiro Oda")),
                      Book("Harry Potter and the Philosopher's Stone",Author("J. K. Rowling")),
                      Book("The Lord of the Rings",Author("John Ronald Reuel Tolkien"))]
        

    def displayBooks(self):
        print()
        for i in range(len(self.books)):
            userBook = self.books[i]
            print(f"{i+1}.",end=" ")
            userBook.giveInfo()
        print()



cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS books")
cursor.execute("CREATE TABLE books (id INT, title STRING, author STRING, isBorrowed BOOLEAN)")

cursor.execute("""
                  INSERT INTO books VALUES 
                  ('1','Quest Of The Sunfish - Escape To The Moon Islands', 'Mardi McConnochie', True),
                  ('2','How To Survive On Mars', 'Jasmina Lazendic-Galloway', False),
                  ('3','One Piece - Volume 1','Eiichiro Oda',False),
                  ('4','Harry Potter and the Philosopher''s Stone','J. K. Rowling',False),
                  ('5','The Lord of the Rings','John Ronald Reuel Tolkien',False)
               """)
connection.commit()
cursor.close()

def displayAllBooks():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    for row in cursor:
           print(f'title: {row["title"]} - {row["author"]}')
    print("\n\n\n")
    cursor.close()
displayAllBooks()

def diaplayAvailableBooks():
    cursor = connection.cursor()
    cursor.execute("SELECT title,isBorrowed,author FROM books WHERE isBorrowed = False")
    for row in cursor:
           print(f'"{row["title"]}" by {row["author"]} is available for borrowing')
    print("\n\n\n")
    cursor.close()
diaplayAvailableBooks()



# myLibrary = Library()
# print("Library menu:")
# while True:
#     userOption = input(" \nOption 1: Display the books.\n Option 2: Borrow a book.\n Option 3: Return a book.\n Option 4: Exit.\n Choose option(1-4):")

#     if userOption == "1":
#         myLibrary.displayBooks()

#     if userOption == "2":
#         myLibrary.displayBooks()
#         userBook = int(input("Please enter the number for your book: "))
#         bookchosen = myLibrary.books[userBook-1]
#         if bookchosen.isBorrowed == False:
#             bookchosen.changeState(True)
#             print(f"You have borrowed {bookchosen.title}.\n")
#         else:
#             print(f"{bookchosen.title} is already borrowed.")

#     if userOption == "3":
#         myLibrary.displayBooks()
#         userBook = int(input("Please enter the number for your book: "))
#         bookchosen = myLibrary.books[userBook-1]
#         if bookchosen.isBorrowed == True:
#             bookchosen.changeState(False)
#             print(f"You have returned {bookchosen.title}.\n")
#         else:
#             print(f"{bookchosen} is not borrowed.")

#     if  userOption == "4":
#         print("\nClosing Library Menu...\n\n")
#         exit()


