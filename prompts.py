#import funtions from items
from Items import get_color, get_size, get_price, get_type
def choice(x, all_items): #function for input from prompt1 in main
    if x == 1:
        myColor = input("What color would you like to search?") #search criteria
        found = False #match is set to False
        available_colors = [] #new list for available options

        for item in all_items: #go through all_items list
            if item.isColor(myColor): #if match print item
                found = True
                print(item)

        if not found: #no matches if statement
            print('Not Available')
            available_colors = get_color(all_items) #get available options
            print("Available choices:", ", ".join(available_colors)) #offer available options for new search

    elif x == 2:

        myType = input("What type of clothes are you looking for?")
        found = False
        available_type = []

        for item in all_items:
            if item.isType(myType):
                found = True
                print(item)
        if not found:
            print('Not Available')
            available_type = get_type(all_items)
            print("Available choices:", ",".join(available_type))

    elif x == 3:

        mySize = input("What size of clothes are you looking for?")
        found = False
        available_size = []
        for item in all_items:
            if item.isSize(mySize):
                found = True
                print(item)
        if not found:
            print('Not Available')
            available_size = get_size(all_items)
            print("Available choices:", ",".join(available_size))

    elif x == 4:

        myPrice = input("What price of clothes are you looking for?")
        found = False
        available_price = []
        for item in all_items:
            if item.isPrice(int(myPrice)):
                found = True
                print(item)
        if not found:
            print('Not Available')
            available_price = get_price(all_items)
            print("Available choices:", ",".join(map(str,available_price)))




