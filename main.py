#import functions to main
from file_access import read_items
from prompts import choice

if __name__ == '__main__':

    all_items = read_items()

    while True: #main loop
        try:
            prompt1 = int(input('How would you like to search: \n1. Color \n2. Type \n3. Size \n4. Price \n5. Quit \n'))

            if prompt1 < 1 or prompt1 > 5: #make sure input is valid
                print('Invalid Selection. Please enter a number: 1-5.')
                continue

            choice(prompt1, all_items) #run search based on prompt1

            if prompt1 == 5: #exit
                print('Goodbye!')
                break
        except ValueError: #invalide selection check
            print('Invalid Selection. Please enter a number: 1-5.')

        while True: #repeat search loop
            continue_search = input('Do you want to continue searching? (Y/N): ').upper()
            if continue_search == 'Y' or continue_search == 'N':
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

        if continue_search == 'N': #exit repeat loop
            print('Goodbye!')
            break




