
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
    with open('Library.csv', 'r') as file1:
        reader = csv.DictReader(file1)
        with open('Library.csv' , 'w') as file2:
            writer = csv.writer(file2)
            for row in reader:
                if row['BookID'] == bookID:
                    writer.writerow(newbook)
                else:
                    writer.writerow(row)
        
 


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
            

    


