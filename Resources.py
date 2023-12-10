import csv
import Data_persistance
csvfile = Data_persistance

class use_resources:
    def list_resources(self):
        with open('Library.csv' , 'r') as f1:
            data = csv.DictReader(f1)
            for book in data:
                print(book['BookName'], 'by', book['Author'], '- Available.')
            
