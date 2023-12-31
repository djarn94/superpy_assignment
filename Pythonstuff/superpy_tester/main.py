# Imports
from argparse import *
import csv
from functions_csv import *
from functions import *
from datetime import date

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

def main():

    #Argparse superpy main
    parser = ArgumentParser(
        description="Welcome to the store of Superpy",
        epilog="Have fun doing stuff!")

    #Menu holder for subparsers
    subparsers = parser.add_subparsers(dest="command")

    ##########################################################################################################################################
    #Bought sub_parser
    bought_parser = subparsers.add_parser(
        "bought", help='Use this function to register bought articles in the following order: 1.product name, 2.buy price, 3.expiration date')

    #bought options
    bought_parser.add_argument("product_name",type = str, help = 'product name as string')
    bought_parser.add_argument("buy_price",type = float, help ='fill in a number as float')
    bought_parser.add_argument("expiration_date",type = str, help = 'fill in expiration date in the following format : YYYY-MM-DD')
    ##########################################################################################################################################

    ##########################################################################################################################################
    #Sold sub_parser
    sold_parser = subparsers.add_parser(
        "sold", help='Use this function to register sold articles in the following order : 1.bought id, 2.sell price')


    #Sold options
    sold_parser.add_argument('bought_id',type = int, help = 'fill in the bought id here as int')
    sold_parser.add_argument('sell_price', type = float, help = 'fill in a number as float')

    ##########################################################################################################################################

    ##########################################################################################################################################
    #Inventory sub_parser
    inventory_parser = subparsers.add_parser(
        'inventory',
        help='Use this function to see the current inventory of the store')

    #Inventory options
    inventory_parser.add_argument('--now', help='show inventory of todays date')
    inventory_parser.add_argument('--boughtlist', help= 'show list of all rows in bought.csv')
    inventory_parser.add_argument('--soldlist', help='show list of sold products')
    inventory_parser.add_argument('--inventory_of_date', help= 'fill in date in format YYYY-MM-DD to see the inventory of that date')
    ##########################################################################################################################################

    ##########################################################################################################################################
    #time_travel sub_parser
    time_travel_parser = subparsers.add_parser(
        'time_travel',
        help=
        'use this function to advance or go back in time. example -2 to go back 2 days or just 2 to advance 2 days')

    #Time travel options
    time_travel_parser.add_argument('set_date',type = str, help='select a date of choice in the following format : YYYY-MM-DD')


    ##########################################################################################################################################
    #Exporter
    export_parser = subparsers.add_parser('export', help='use this to export certain data')

    export_parser.add_argument('-bought', help='use this to export all bought data to today')
    #Parse arguments
    args = parser.parse_args()


    if args.command == 'bought':
        buy_product(args.product_name, args.buy_price, args.expiration_date)
        print(f"bought {args.product_name}('s) has been registered with succes. with a price off {args.buy_price}.")
    elif args.command == 'sold':
        sell_product(args.bought_id, args.sell_price)
        print(f'Product has been registered in sold.csv')
    elif args.command == 'time_travel':
            if args.set_date == 'today' :
                change_date(date.today())
            else:
                 try:
                    date.fromisoformat(args.set_date)
                    change_date(args.set_date)
                 except ValueError:
                     raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    elif args.command == 'export':
        export_bought()
        print(f'Export has been created in the following folder : C:/Pythontester/superpy_tester/bought_exports. \nIf folder does not exist one will be made.')
    else:
        pass

if __name__ == "__main__":
    main()
    print('use -h for a list of commands')
    print(f'date: {date_today()}')
