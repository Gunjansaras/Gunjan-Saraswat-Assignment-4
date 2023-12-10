import pandas as pd 
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

      
def edit_data(bookID, bookname, Newvalue):
    f1 = pd.read_csv('Library.csv')
    f1.loc[bookID, 'BookName'] = Newvalue
    f1.to_csv('Library.csv' , index = False)
    print(f1)

def delete_data(bookname):
    f1 = pd.read_csv('Library.csv' , index_col='BookName')
    f1 = f1.drop(f1[f1.BookName == bookname].index)
    f1.to_csv('Library.csv', index=False)



   
    


