from datetime import date
import csv
import itertools
from rich.table import Table
from rich.console import Console
from collections import Counter

     
today = str(date.today())

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
    
def inventory_list():
     
     with open('bought.csv', 'r', newline = '') as file:
         csv_reader = csv.DictReader(file)
         product_list = []
         id_list = []

         table = Table(title=f'Inventory')
         table.add_column("Product name", justify="left", style="cyan", no_wrap=True)
         table.add_column("Amount", justify="center", style="magenta")

         for id in csv_reader:
            id_list.append(id['id']) 
            if id_list not in get_bought_id():
                for col in csv_reader:
                    product_list.append(col['product_name'])

         product_dict = dict((x, product_list.count(x)) for x in set(product_list))
         for product, amount in product_dict.items():
             table.add_row(product, str(amount))

         return table

def bought_list():

     list = []
     
     table = Table(title=f'bought list')
     table.add_column("id", justify="left", style="cyan", no_wrap=True)
     table.add_column("product name", justify="center", style="magenta")
     table.add_column("buy price", justify="center", style="magenta")
     table.add_column("buy date", justify="center", style="magenta")
     table.add_column("expiry date", justify="center", style="magenta")
     table.add_column('expired', justify='center',style='red')

     with open('bought.csv', 'r', newline = '') as file:
         csv_reader = csv.reader(file)
         next(csv_reader, None)

         for row in csv_reader:
            list.append(row)
     
         
     for id, product, price, date, exp in list:
         if exp < today :
            table.add_row(id, product, price, date, exp, 'x')
         else:
            table.add_row(id, product, price, date, exp)

     return table

def sold_list():

     table = Table(title=f'sold list')
     table.add_column("id", justify="left", style="cyan", no_wrap=True)
     table.add_column("bought id", justify="center", style="magenta")
     table.add_column("sell price", justify="center", style="magenta")
     table.add_column("sell date", justify="center", style="magenta")

     with open('sold.csv', 'r', newline = '') as file:
         reader = csv.reader(file)
         next(reader, None)

         for id,boughtid,sell,date in reader:
            table.add_row(id,boughtid,sell,date)

     return table

#Gets a list of bought_id's in the sold.csv file
def get_bought_id():
         
    with open('sold.csv', 'r', newline = '') as sold_file:
         next
         sold_reader = csv.DictReader(sold_file)
         sold_rows = list(sold_reader)

    for row in sold_rows:
        return list(row['bought_id'])


####  test  ####
def inventory_now():
    today = date.today
    
    with open('bought.csv', 'r', newline = '') as file:

        table = table(title = 'inventory')

        table.add_column('product_name', style = 'white')
        table.add_column('amount', style = 'white')
        table.add_column('expiry_date', style = 'white')

    for row in inventory_list:
        table.add_row(row)


     
    
    

    
