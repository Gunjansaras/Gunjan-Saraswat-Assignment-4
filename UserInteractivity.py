import Resource_management
class Interaction:
    def __init__(self):
        print('Welcome to the Library system!')
    def create(self):
        book_ID = int(input('Enter Book ID: '))
        book_name = input('Enter book name: ')
        Subject = input('Enter the subject of the book 1.novel or 2.Course book: ')
        Language = input('Enter the language of the book: ')
        Author_name = input('Enter the name of the Author: ')
        Date_of_publication = input('Enter the date of publication: ')
        Book = {'Book ID' : book_ID, 'Book Name' : book_name, 'Subject' : Subject, 'Language' : Language, 'Author Name' : Author_name, 'Date of Publication' : Date_of_publication}  
        manager1 = Resource_management.manager()      
        print(manager1.addbook(Book))


        
