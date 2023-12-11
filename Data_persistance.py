import pandas as pd   #importing pandas module 
import csv           #importing csv module 

f1 = open('Library.csv' , 'w', newline='')
data = csv.writer(f1)
header = ['BookID', 'BookName','Author', 'Language', 'Date of publication', 'Status']
data.writerow(header)
f1.close()      #write row of header 

def enterdata(book):     #entering data in the form of lists 
    f1 = open('Library.csv' , 'a', newline='')
    data = csv.writer(f1)
    data.writerow(book)
    f1.close()

      
def editdata(bookID, Newvalue):
    f1 = pd.read_csv('Library.csv')          #editing name of the book
    f1.loc[bookID, 'BookName'] = Newvalue
    f1.to_csv('Library.csv' , index = False)
    print(f1)
 
def delete_data(bookname):                 #deleting rows from the file 
    f1 = pd.read_csv('Library.csv' , index_col='BookName')
    f1 = f1.drop(f1[f1.BookName == bookname].index)
    f1.to_csv('Library.csv', index=False)



   
    


