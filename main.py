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
    time_travel_parser.add_argument('--advance_time',type = int, help='advance or go back in time by entering a number use - to go back in time')

    ##########################################################################################################################################

    #Parse arguments
    args = parser.parse_args()


    if args.command == 'bought':
        buy_product(args.product_name, args.buy_price, args.expiration_date)
        print(f"bought {args.product_name}('s) has been registered with succes. with a price off {args.buy_price}.")
    elif args.command == 'sold':
        sell_product(args.bought_id, args.sell_price)
        print(f'Product has been registered in sold.csv')
    elif args.command == 'inventory':
        if args.now == 'now':
            console.print(inventory_list())
        if args.boughtlist == 'boughtlist':
            console.print(bought_list())
        if args.soldlist == 'sold':
            console.print(sold_list())
    else:
        pass

if __name__ == "__main__":
    console = Console()
    print('use -h for a list of commands')
    main()
