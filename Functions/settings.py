import csv
from pathlib import *
from datetime import datetime
from datetime import timedelta
from datetime import date

#Returns current date (which can be changed by using change_date function).
def date_today():
   with open('data/time.csv', 'r') as file:
      next(file)
      reader = csv.reader(file)
      list = []
      for line in reader:
         list.append(line)

      return list[0][1]

def change_date(date):

      file = csv.reader(open('data/time.csv'))
      reader  = list(file)

      reader[1][1] = date
      
      writer = csv.writer(open('data/time.csv', 'w', newline=''))
      writer.writerows(reader)

def advance_date(number):

   current_date = date_today()
   current_date_temp = datetime.strptime(current_date, "%Y-%m-%d")
   newdate = current_date_temp + timedelta(days=number)
   file = csv.reader(open('data/time.csv'))
   reader  = list(file)

   reader[1][1] = datetime.date(newdate)
   writer = csv.writer(open('data/time.csv', 'w', newline=''))
   writer.writerows(reader)