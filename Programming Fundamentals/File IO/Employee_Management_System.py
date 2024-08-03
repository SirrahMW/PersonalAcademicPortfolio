import pickle


# Establish the employee class #
class Employee:
    def __init__(self, name, emp, dept, title):
        self.name = name
        self.empID = emp
        self.dept = dept
        self.title = title
   
    # Accessor methods #
    def Name(self):
        return self.name
    
    def Employee_ID(self):
        return self.empID

    def Department(self):
        return self.dept

    def Job_Title(self):
        return self.title


# Constants #
LOOKUP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILE = 'employees.dat'


# Function to load employees from the file #
def Load():
    # Try to load the dictionary from a file #
    try:
        with open(FILE, 'rb') as file:
            employees = pickle.load(file)
    # Create empty dictionary if it doesn't exist #
    except IOError:
        employees = {}
    # Return dict #
    return employees


# Function to create the menu #
def Get_Menu_Choice():
    # The menu #
    print('\nEmployee Management System:\n')
    print('1.\tLookup employee')
    print('2.\tAdd a new employee ID')
    print('3.\tChange employee information')
    print('4.\tDelete an employee ID')
    print('5.\tExit\n')
    # Get user input #
    choice = int(input('Enter: '))
    print()
    # Validate input #
    while choice < LOOKUP or choice > QUIT:
        choice = int(input('Please make a valid selection: '))
    # Return input #
    return choice


# Function to look up an employee #
def Lookup(employees):
    # User search #
    search = int(input('Enter an ID to look up: '))
    if search in employees:
        print('Name:', employees[search].Name())
        print('Department:', employees[search].Department())
        print('Job Title:', employees[search].Job_Title())


# Function to add an employee #
def Add(employees):
    name = input('Employee name: ')
    emp_id = int(input('Employee ID: '))
    dept = input('Employee department: ')
    title = input('Employee job title: ')
    # Create new employee object #
    new = Employee(name, id, dept, title)
    # If the entry doesn't exist #
    if emp_id not in employees:
        employees[emp_id] = new
        print('Entry made.')
    # If it does #
    else:
        print('Entry already exists.')


# Function to change employee info #
def Change(employees):
    # Search term #
    search = int(input('Enter an ID to change data for: '))
    # If the ID exists #
    if search in employees:
        # New information #
        name = input('Employee name: ')
        dept = input('Employee department: ')
        title = input('Employee job title: ')
        new = Employee(name, id, dept, title)
        # Update the information #
        employees[search] = new
        print('Entry updated.')
    # If the ID does not exist #
    else:
        print('Entry does not exist.')


def Delete(employees):
    # Search term #
    search = int(input('Enter an ID to delete: '))
    # If ID exists, delete it #
    if search in employees:
        del employees[search]
        print('Entry deleted.')
    # If it doesn't exist, do nothing #
    else:
        print('Entry does not exist.')


# Function to save to a file #
def Save(employees):
    # Open file and dump #
    with open(FILE, 'wb') as file:
        pickle.dump(employees, file)


# Main function #
def main():
    # Load the dictionary from file #
    employees = Load()
    # Initialize choice #
    choice = 0
    # Run program until user hits quit #
    while choice != QUIT:
        # Get choice #
        choice = Get_Menu_Choice()
        # Decide what function to use #
        if choice == LOOKUP:
            Lookup(employees)
        elif choice == ADD:
            Add(employees)
        elif choice == CHANGE:
            Change(employees)
        elif choice == DELETE:
            Delete(employees)
    # Save new file before close #
    Save(employees)
    print('File saved as:', FILE)


# Run #
main()
