
import csv

f1 = open('Library.csv' , 'w')
data = csv.writer(f1)
header = [' BookID ' ' BookName ' ' Author ' ' Language ' ' Date of publication ' ' Status ']
data.writerow(header)

f1.close()

def enterdata(book):
    f1 = open('Library.csv' , 'a')
    data =data = csv.writer(f1)
    data.writerow(book)
    f1.close()

            

    


