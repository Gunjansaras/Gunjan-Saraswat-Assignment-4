import csv
import Data_persistance

class use_resources:
    def __init__(self):
        self.f1 = open('Library.csv', 'r')
        self.data = csv.reader(self.f1)
    def list_resources(self):
        for book in self.data:
            return f"{book[1]} by {book[2]} - Available."
    def check_out(self, bookname, bookauthor):
        for book in self.data:
            if book[1] == bookname:
                self.data.remove(book)
                return f"{bookname} by {bookauthor} - Checked out."
            else:
                return f"{bookname} by {bookauthor} - Unavailable."
    def returnbook(self, bookname, bookauthor, book):
        for book in self.data:
            book[1] == bookname
            self.data.append(book)
            return f"{bookname} by {bookauthor} - Returned."
    



    
    