class manager: 
    def __init__(self):
        self._collection = []
    def addbook(self, book = {}):
        self._collection.append(book)
        return self._collection
    def search(self, choice, book_attribute):
        if choice == 1:
            for book in self._collection:
                if book[0] == book_attribute:
                    return (f"{book[1]} by {book[5]} is available.")
                else:
                    return 'Book Not Found'
        elif choice == 2:
            for book in self._collection:
                if book[1] == book_attribute:
                    return (f"{book[1]} by {book[5]} is available.")
                else:
                    return 'Book Not Found'
        else:
            return 'Invalid Book attribute!'
    def Edit(self, bookID, bookname, subject, language, authorname, date):
        for book in self._collection:
            if book[0] == bookID:
                book = {'Book ID' : bookID, 'Book Name' : bookname, 'Subject' : subject, 'Language' : language, 'Author name' : authorname, 'Date of publication' : date}
                return book
        return self._collection
    def delete(self, bookID):
        for book in self._collection:
            if book[0] == bookID:
                print(book.pop(bookID))
            return self._collection
    def getlist(self):
        return self._collection


            
                
                


