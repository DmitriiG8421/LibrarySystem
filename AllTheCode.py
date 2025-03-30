class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.isBorrowed = False

class Library:
    def __init__(self):
        self.books = [Book("Quest Of The Sunfish - Escape To The Moon Islands", Author("Mardi McConnochie")),
                      Book("How To Survive On Mars", Author("Jasmina Lazendic-Galloway")),
                      Book("One Piece - Volume 1"),Author("Eiichiro Oda"),
                      Book("Harry Potter and the Philosopher's Stone",Author("J. K. Rowling")),
                      Book("The Lord of the Rings"),Author("John Ronald Reuel Tolkien")]
        