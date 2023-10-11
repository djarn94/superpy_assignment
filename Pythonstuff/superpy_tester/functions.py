from datetime import date
import csv
import itertools
from collections import Counter
   

#Generates a bought ID
def bought_id():
    with open('bought.csv', 'r', newline = '') as file:
        csv_reader = csv.DictReader(file)
        rows = list(csv_reader)
        for row in rows:      
            id_list = row['id']
        try:
            last_id = int(id_list[-1]) + 1
        except:
            last_id = 1
        return last_id
    
#generates a sold ID
def sold_id():
    with open('sold.csv', 'r', newline = '') as file:
        csv_reader = csv.DictReader(file)
        rows = list(csv_reader)
        for row in rows:
            id_list = row['id']
        try:
            last_id = int(id_list[-1]) + 1
        except:
            last_id = 1
        return last_id
    
today = str(date.today())
match today:
    case '-today':
        today = str(date.today())
    case '-any':
        today = input("please set your date(format YYYY-MM-DD): ")
     
    
    

    
