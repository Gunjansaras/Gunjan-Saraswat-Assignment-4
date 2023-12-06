
class manager: 
    def __init__(self)
        self._collection = []
    def addbook(self, book):
        self._collection.append(book)
        return self._collection
    def search(self, book_attribute):
        if type(book_attribute) == int:
            for book in self._collection:
                if book[0] == book_attribute:
                    return book
                else:
                    return 'Book Not Found'
        elif type(book_attribute) == str:
            for book in self._collection:
                if book[1] == book_attribute:
                    return book
                else:
                    return 'Book Not Found'
        else:
            return 'Invalid Book attribute!'
    