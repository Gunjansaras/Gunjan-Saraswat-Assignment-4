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
            bookID = int(input('Enter the ID of the book that you want to find: '))             
            print(manager1.search(choice, bookID))
        elif choice == 2:
            bookname = input('Enter the name of the book: ')
            print(manager1.search(choice, bookname))
        else:
            print('Invalid choice!')   
    def edit(self):
        select_bookID = int(input('Enter Book ID: '))
        newbookname = input('Enter new book name: ')
        newLanguage = input('Enter the new language: ')
        newAuthor = input("Enter the new book's Author's name: ")
        newDate = input('Enter the new date: ')
        print(manager1.Edit(select_bookID, newbookname, newAuthor, newLanguage, newDate))
        newbook = [select_bookID, newbookname, newAuthor, newLanguage, newDate, 'Available']
        addbook = csvfileopen.editdata(select_bookID, newbook)
    def delete(self):
        bookname = input('Enter the book name: ')
        print(manager1.delete(bookname))
        deletebook = csvfileopen.delete_data(bookname)




interaction1 = Interaction()
csvfileopen = Data_persistance

book1 = [101, 'Origin', 'Dan Brown', 'English', 2017, 'Available']
manager1 = Resource_management.manager(101, 'Origin', 'Dan Brown', 'English', 2017, 'Available')
interaction1.create(101, 'Origin', 'Dan Brown', 'English', 2017, 'Available')
print('Origin by Dan brown (2017) - Available')


book2 = [102, 'Pride & Prejudice', 'Jane Austen', 'English', 1813, 'Available']
manager1 = Resource_management.manager(102, 'Pride & Prejudice', 'Jane Austen', 'English', 1813, 'Available')
interaction1.create(102, 'Pride & Prejudice', 'Jane Austen', 'English', 1813, 'Available')
print('Pride & Prejudice by Jane Austen (1813) - Available.')



while True:
    choice = int(input('Choose among the following. \n 1.Create \n 2.Read \n 3.Edit \n 4.Delete \n 5.Exit '))
    if choice == 1:
        book_ID = int(input('Enter Book ID: '))
        book_name = input('Enter book name: ')
        Language = input('Enter the language of the book: ')
        Author_name = input('Enter the name of the Author: ')
        Date_of_publication = input('Enter the date of publication: ')
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


def resources_menu():
    while True:
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









             
        
