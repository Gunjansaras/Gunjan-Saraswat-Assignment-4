import Resource_management 
class Interaction:
    def __init__(self):
        print('Welcome to the Library system!')
        self.newbook = None
    def create(self, book_ID, book_name, Author_name, Language, Date_of_publication):
        self.newbook = Resource_management.manager(book_ID, book_name, Author_name, Language, Date_of_publication )
        manager1.addbook(self.newbook)
        
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
        select_book = int(input('Enter Book ID: '))
        newbookname = input('Enter new book name: ')
        newsubject = input('Enter new subject: ')
        newLanguage = input('Enter the new language: ')
        newAuthor = input("Enter the new book's Author's name: ")
        newDate = input('Enter the new date: ')
        manager1 = Resource_management.manager()
        print(manager1.Edit(select_book, newbookname, newsubject, newLanguage, newAuthor, newDate))
    def delete(self):
        bookID = int(input('Enter the book ID: '))
        manager1 = Resource_management.manager()
        print(manager1.delete(bookID))


interaction1 = Interaction()
i = 1
while True:
    print(f"Entering book {i} details")
    book_ID = int(input('Enter Book ID: '))
    book_name = input('Enter book name: ')
    Language = input('Enter the language of the book: ')
    Author_name = input('Enter the name of the Author: ')
    Date_of_publication = input('Enter the date of publication: ')
    manager1 = Resource_management.manager(book_ID, book_name, Author_name, Language, Date_of_publication )
    print(interaction1.create(book_ID, book_name, Author_name, Language, Date_of_publication))
    add_more = input('Do you want to add more books to the Library? y/n: ')
    i+=1
    if add_more.lower() == 'n':
        break
def menu():
    while True:
        choice = int(input('Choose among the following. \n 1.Create \n 2.Read \n 3.Edit \n 4.Delete \n 5.Exit '))
        if choice == 1:
            book_ID = int(input('Enter Book ID: '))
            book_name = input('Enter book name: ')
            Language = input('Enter the language of the book: ')
            Author_name = input('Enter the name of the Author: ')
            Date_of_publication = input('Enter the date of publication: ')
            manager1 = Resource_management.manager(book_ID, book_name, Author_name, Language, Date_of_publication )
            print(interaction1.create(book_ID, book_name, Author_name, Language, Date_of_publication))
        elif choice == 2:
            print(interaction1.Read())
        elif choice == 3:
            print(interaction1.edit())
        elif choice == 4:
            print(interaction1.delete())
        else:
            print('Exiting the Program!')
            break

menu()









             
        
