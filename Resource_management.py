
class manager: 
    def __init__(self, BookID, Bookname, Author, Language, Date_of_publication, Availability):
        self._collection = []
        self._bookID = BookID
        self._bookname = Bookname
        self._author = Author
        self._language = Language
        self._DOP = Date_of_publication
        self._availability = Availability
    def getbookID(self):
        return self._bookID
    def getbookName(self):
        return self._bookname
    def getAuthor(self):
        return self._author
    def getdate(self):
        return self._DOP
    def setbookName(self, newbookName):
        self._bookname = newbookName
    def setAuthor(self, newAuthor):
        self._author = newAuthor
    def setLanguage(self, newLanguage):
        self._language = newLanguage
    def setDOP(self, newDOP):
        self._DOP = newDOP
    def set_status(self, newstatus):
        self._availability = newstatus
    def addbook(self, book_object):
        self._collection.append(book_object)
        return self._collection

    def search(self, choice, book_attribute):
        if choice == 1:
            for book in self._collection:
                if (book.getbookID() == book_attribute):
                    return (f"{book.getbookName()} by {book.getAuthor()} - Available.")
                else:
                    return book.getbookID()
        elif choice == 2:
            for book in self._collection:
                if (book.getbookName() == book_attribute):
                    return (f"{book.getbookName()} by {book.getAuthor()} - Available.")
                else:
                    return book.getbookName()
        else:
            return 'Invalid Book attribute!'
    def Edit(self, bookID, newbookname, newauthorname, newlanguage, newdate):
        for book in self._collection:
            if book.getbookID() == bookID:
                book.setbookName(newbookname)
                book.setLanguage(newlanguage)
                book.setAuthor(newauthorname)
                book.setDOP(newdate)
    def delete(self, bookname):
        for book in self._collection:
            if book.getbookName() == bookname:
                self._collection.remove(book)
                return 'Book Removed!'
            else:
                return 'Book not found!'
    def getlist(self):
        return self._collection
                



            
                
                


