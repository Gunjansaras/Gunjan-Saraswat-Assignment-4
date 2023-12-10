
import csv

f1 = open('Library.csv' , 'w', newline='')
data = csv.writer(f1)
header = ['BookID', 'BookName','Author', 'Language', 'Date of publication', 'Status']
data.writerow(header)
f1.close()

def enterdata(book):
    f1 = open('Library.csv' , 'a', newline='')
    data =data = csv.writer(f1)
    data.writerow(book)
    f1.close()

def editdata(bookID,  newbook):
    f1 = open('Library.csv' , 'w', newline='')
    f2 = open('Library.csv', 'r')
    writer = csv.writer(f1)
    reader = csv.reader(f2)
    for book in reader:
        if book[0] == bookID:
            writer.writerow(newbook)
        else:
            writer.writerow(book)
    f1.close()
    f2.close()


def delete_data(bookname):
    f1 = open('Library.csv', 'r')
    f2 = open('Library.csv', 'w', newline='')
    writer = csv.writer(f2)
    reader = csv.reader(f1)
    for row in reader:
        if row[1] != bookname:
            writer.writerow(row)
    f1.close()
    f2.close()
            

    


