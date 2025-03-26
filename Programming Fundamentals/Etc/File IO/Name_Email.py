# Use pickling #
import pickle

# Constants for user menu interface #
LOOKUP = 1
NEW = 2
CHANGE = 3
DELETE = 4
QUIT = 5


# Function for looking up a key in the dict #
def lookup_email(data):
    # User input #
    name = input('Name: ')
    # Searching the dict #
    for entry in data:
        if entry == name:
            print(data[entry])


# Function to create a new key in the dict #
def add_email(data):
    # User input #
    name = input('Name: ')
    email = input('Email: ')
    # If it doesn't exist, create it #
    if name not in data:
        data[name] = email
    else:
        print('Entry already exists.')


# Function to edit an existing key in the dict #
def change_email(data):
    # User input #
    name = input('Name: ')
    email = input('New email: ')
    # If it exists, change it #
    if name in data:
        data[name] = email
    else:
        print('No entry exists.')


# Function to delete a key in the dict #
def delete_email(data):
    # User input #
    name = input('Name: ')
    # If it exists, delete it #
    if name in data:
        del data[name]
    else:
        print('No entry exists.')


# Funtion to create the menu and get an input from the user #
def get_menu_choice():
    print('Email lookup tool')
    print('--------------------')
    print('1. Lookup a name')
    print('2. Create new entry')
    print('3. Change an entry')
    print('4. Delete an entry')
    print('5. Quit')
    print()
    # Collect the user choice #
    choice = int(input())
    # Validate that it is a valid input #
    while choice < LOOKUP or choice > QUIT:
        choice = int(input('Please input a valid choice: '))
    # Return the choice to the function call #
    return choice


# Main function #
def main():
    # Unpickle the dict #
    with open('info.dat', 'rb') as data:
        emails = pickle.load(data)
    # Variable for user's choice #
    choice = 0
    # Unless the user quits, keep allowing new input #
    while choice != QUIT:
        choice = get_menu_choice()
        # Determine user's desired function #
        if choice == LOOKUP:
            lookup_email(emails)
        elif choice == NEW:
            add_email(emails)
        elif choice == CHANGE:
            change_email(emails)
        elif choice == DELETE:
            delete_email(emails)
    # Pickle the newly edited dict #
    with open('info.dat', 'wb') as data:
        pickle.dump(emails, data)


# Call on the main function #
main()
