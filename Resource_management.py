class manager: 
    def __init__(self, BookID, Bookname, Author, Language, Availability):
        self._collection = []
        self._bookID = BookID
        self._bookname = Bookname
        self._author = Author
        self._language = Language
        self._availability = Availability
    def getbookID(self):
        return self._bookID
    def getbookName(self):
        return self._bookname
    def getAuthor(self):
        return self._author  
    def addbook(self, book_object):
        self._collection.append(book_object)
        return self._collection

    def search(self, choice, book_attribute):
        if choice == 1:
            for book in self._collection:
                if (book.getbookID() == book_attribute):
                    return (f"{book.getbookName()} by the author {book.getAuthor()} is available.")
                else:
                    return "Book not found!"
        elif choice == 2:
            for book in self._collection:
                if (book.getbookName() == book_attribute):
                    return (f"{book.getbookName()} by the author {book.getAuthor()} is available.")
                else:
                    return book.getbookName()
        else:
            return 'Invalid Book attribute!'
    def Edit(self, bookID, bookname, subject, language, authorname, date):
        for book in self._collection:
            if book[0] == bookID:
                book = {'Book ID' : bookID, 'Book Name' : bookname, 'Subject' : subject, 'Language' : language, 'Author name' : authorname, 'Date of publication' : date}
                return self._collection
            else:
                return 'Book not found!'
    def delete(self, bookID):
        for book in self._collection:
            if book[0] == bookID:
                book.pop(bookID)
                return self._collection
            else:
                return 'Book not found!'
                
    def getlist(self):
        return self._collection


            
                
                


