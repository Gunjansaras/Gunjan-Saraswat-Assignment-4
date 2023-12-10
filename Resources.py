import csv
import Data_persistance
csvfile = Data_persistance

class use_resources:
    def list_resources(self):
        with open('Library.csv' , 'r') as f1:
            data = csv.DictReader(f1)
            for book in data:
                print(book['BookName'], 'by', book['Author'], '- Available.')
            
    def check_out(self, bookname):
        with open('Library.csv' , 'r') as f1:
            data = csv.DictReader(f1)
            for row in data:
                if row['BookName'] == bookname:
                    csvfile.delete_data(bookname)
                    return(f"{row['BookName']} by {row['Author']} - Issued successfully.")
                else:
                    pass
            else:
                return (f"{row['BookName']} by {row['Author']} - Unavailable.")
                    


    
    



    
    