
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
            

    


