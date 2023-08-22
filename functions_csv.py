from datetime import date
import csv
from functions import *
from rich.console import Console

def buy_product(product_name, buy_price, expiration_date):

  today = date.today()
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
      'buy_date' : today,
      'expiration_date' : exp_date
    }
    csv_writer = csv.DictWriter(file,fieldnames=fieldnames)
    csv_writer.writerow(add)

def sell_product(bought_id, sell_price):
    
    today = date.today()

    with open('sold.csv', 'a', newline='') as file:
      fieldnames = ['id',
                    'bought_id',
                    'sell_price',
                    'sell_date']
      add = {
        'id' : sold_id(),
        'bought_id' : bought_id,
        'sell_price' : sell_price,
        'sell_date' : today}
      csv_writer = csv.DictWriter(file,fieldnames=fieldnames)
      csv_writer.writerow(add)