#importing necessary modules 
import csv
import Resource_management 
import Data_persistance
import Resources
class Interaction:
    def __init__(self):
        print('Welcome to the Library system!')
        self.newbook = None
    def create(self, book_ID, book_name, Author_name, Language, Date_of_publication, status):
        self.newbook = Resource_management.manager(book_ID, book_name, Author_name, Language, Date_of_publication, status )
        manager1.addbook(self.newbook)
        addbookdetails = [book_ID, book_name, Author_name, Language, Date_of_publication, status]        
        addbook = csvfileopen.enterdata(addbookdetails)
        
    def Read(self):
        choice = int(input('By which attribute do you want to find the book 1.BookID 2.Bookname? '))
        if choice == 1:
            try:
                bookID = int(input('Enter the ID of the book that you want to find: '))
            except ValueError:
                bookID = int(input('Invalid choice! Enter the ID of the book again: '))            
            print(manager1.search(choice, bookID))
        elif choice == 2:
            try:
                bookname = input('Enter the name of the book: ')
                if bookname.isdigit() == True:
                    raise ValueError
            except:
                bookname = input('Invalid choice! Enter the name of the book again: ')
            print(manager1.search(choice, bookname))
        else:
            print('Invalid choice!')   
    def edit(self):
        try:
            select_bookID = int(input('Enter Book ID: '))
        except ValueError:
            print('Invalid input, Try again!')
            select_bookID = int(input('Enter Book ID again: '))
        try:
            newbookname = input('Enter book name: ')
            if newbookname.isdigit() == True:
                raise ValueError
        except ValueError:
            print('Invalid input, Try again!')
            newbookname = input('Enter book name again: ')
        try:
            newLanguage = input('Enter the language of the book: ')
            if Language.isdigit() == True:
                raise ValueError
        except ValueError:
            print('Invalid input, Try again!')
            newLanguage = input('Enter the language of the book again: ')
        try:
            newAuthor = input('Enter the name of the Author: ')
            if newAuthor.isdigit() == True:
                raise ValueError
        except ValueError:
            print('Invalid input, Try again!')
            newAuthor = input('Enter the name of the Author again: ')
        try:
            newDate = input('Enter the date of publication: ')
            if newDate.isalpha() == True:
                raise ValueError
        except ValueError:
            print('Invalid input, Try again!')
            newDate = input('Enter the date of publication again: ') 
            print(manager1.Edit(select_bookID, newbookname, newAuthor, newLanguage, newDate))
        newbook = [select_bookID, newbookname, newAuthor, newLanguage, newDate, 'Available']
        addbook = csvfileopen.editdata(select_bookID, newbook)
    def delete(self):
        bookname = input('Enter the book name: ')
        print(manager1.delete(bookname))
        deletebook = csvfileopen.delete_data(bookname)


interaction1 = Interaction()
csvfileopen = Data_persistance

#ready test cases 
book1 = [101, 'Origin', 'Dan Brown', 'English', 2017, 'Available']
manager1 = Resource_management.manager(101, 'Origin', 'Dan Brown', 'English', 2017, 'Available')
interaction1.create(101, 'Origin', 'Dan Brown', 'English', 2017, 'Available')
print('Origin by Dan brown (2017) - Available')


book2 = [102, 'Pride & Prejudice', 'Jane Austen', 'English', 1813, 'Available']
manager1 = Resource_management.manager(102, 'Pride & Prejudice', 'Jane Austen', 'English', 1813, 'Available')
interaction1.create(102, 'Pride & Prejudice', 'Jane Austen', 'English', 1813, 'Available')
print('Pride & Prejudice by Jane Austen (1813) - Available.')


while True:
    try:
        choice = int(input('Choose among the following. \n 1.Create \n 2.Read \n 3.Edit \n 4.Delete \n 5.Exit '))
    except ValueError:
        print('invalid choice! Enter in numeric value only.')
        choice = int(input('Choose among the following. \n 1.Create \n 2.Read \n 3.Edit \n 4.Delete \n 5.Exit '))
    if choice == 1:
        try:
            book_ID = int(input('Enter Book ID: '))
        except ValueError:
            print('Invalid input, Try again!')
            book_ID = int(input('Enter Book ID again: '))
        try:
            book_name = input('Enter book name: ')
            if book_name.isdigit() == True:
                raise ValueError
        except ValueError:
            print('Invalid input, Try again!')
            book_name = input('Enter book name again: ')
        try:
            Language = input('Enter the language of the book: ')
            if Language.isdigit() == True:
                raise ValueError
        except ValueError:
            print('Invalid input, Try again!')
            Language = input('Enter the language of the book again: ')
        try:
            Author_name = input('Enter the name of the Author: ')
            if Author_name.isdigit() == True:
                raise ValueError
        except ValueError:
            print('Invalid input, Try again!')
            Author_name = input('Enter the name of the Author again: ')
        try:
            Date_of_publication = input('Enter the date of publication: ')
            if Date_of_publication.isalpha() == True:
                raise ValueError
        except ValueError:
            print('Invalid input, Try again!')
            Date_of_publication = input('Enter the date of publication again: ')   
   
        status = 'Available'
        manager1 = Resource_management.manager(book_ID, book_name, Author_name, Language, Date_of_publication, status)
        print(interaction1.create(book_ID, book_name, Author_name, Language, Date_of_publication, status))
    elif choice == 2:
        print(interaction1.Read())
    elif choice == 3:
        print(interaction1.edit())
    elif choice == 4:
        print(interaction1.delete())
    else:
        print('Exiting the Program!')
        break

#resources menu, accessing functions in the resources module.
def resources_menu():
    while True:
        try:
            choice = int(input('Choose among the following. \n 1.List the books \n 2.Issue a book \n 3.Return a book \n 4.Exit.'))
        except ValueError:
            print('Invalid choice! Enter a numeric value only.')
            choice = int(input('Choose among the following. \n 1.List the books \n 2.Issue a book \n 3.Return a book \n 4.Exit.'))
        if choice == 1:
            print(resources.list_resources())
        elif choice == 2:
            bookname = input('Enter the name of the book that you want to issue: ')
            print(resources.check_out(bookname))
        elif choice == 3:
            book_ID = int(input('Enter Book ID: '))
            book_name = input('Enter book name: ')
            Language = input('Enter the language of the book: ')
            Author_name = input('Enter the name of the Author: ')
            Date_of_publication = input('Enter the date of publication: ')
            status = 'Available'
            book = [book_ID, book_name, Author_name, Language, Date_of_publication, status]
            print(resources.returnbook(book_name, Author_name, book))
            interaction1.delete()
        else:
            print('Exiting the program!')
            break


resources = Resources.use_resources()
resources_menu()







             
        
