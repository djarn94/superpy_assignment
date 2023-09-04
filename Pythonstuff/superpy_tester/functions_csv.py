from datetime import date
import csv
from functions import *
from pathlib import *

def buy_product(product_name, buy_price, expiration_date):

  today_buy = date_today()
  exp_date = date.fromisoformat(expiration_date)

  with open('bought.csv', 'a', newline='') as file:
    fieldnames = ['id',
                  'product_name',
                  'buy_price',
                    'buy_date',
                      'expiration_date']
    add = {
      'id' : bought_id(),
      'product_name' : product_name,
      'buy_price' : buy_price,
      'buy_date' : today_buy,
      'expiration_date' : exp_date
    }
    csv_writer = csv.DictWriter(file,fieldnames=fieldnames)
    csv_writer.writerow(add)

def sell_product(bought_id, sell_price):
    
    today_sell = date_today()

    with open('sold.csv', 'a', newline='') as file:
      fieldnames = ['id',
                    'bought_id',
                    'sell_price',
                    'sell_date']
      add = {
        'id' : sold_id(),
        'bought_id' : bought_id,
        'sell_price' : sell_price,
        'sell_date' : today_sell}
      csv_writer = csv.DictWriter(file,fieldnames=fieldnames)
      csv_writer.writerow(add)


def date_today():
   with open('time.csv', 'r') as file:
      next(file)
      reader = csv.reader(file)
      list = []
      for line in reader:
         list.append(line)

      return list[0][1]

def change_date(date):

      

      file = csv.reader(open('time.csv'))
      reader  = list(file)

      reader[1][1] = date
      
      writer = csv.writer(open('time.csv', 'w', newline=''))
      writer.writerows(reader)


def export_bought():
   
   path = Path.cwd() / "bought_exports"
   path.mkdir(exist_ok=True)


   with open('bought.csv', 'r', newline = '') as file:
      csv_reader = csv.DictReader(file)
      rows = list(csv_reader)

   file_name = 'bought_export_' + date_today()

   fpath = (path / file_name).with_suffix('.csv')   
   with fpath.open('w', newline='') as new_file:
      writer= csv.DictWriter(new_file, fieldnames = 
                              ['id',
                  'product_name',
                  'buy_price',
                    'buy_date',
                      'expiration_date'])
      
      writer.writeheader()
      for row in rows:
          writer.writerow(row)
      print(f'Export has been created in the following folder : {path}. \nIf folder does not exist one will be made.')