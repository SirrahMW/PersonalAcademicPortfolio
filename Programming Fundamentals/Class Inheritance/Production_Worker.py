import Employee

# Washington minimum wage #
MINWAGE = 15.74

def main():
    # Collect user input #
    print('Enter an new Production Worker\'s information:')
    name = input('Name: ')
    empNum = int(input('Employee Number: '))
    shiftNum = int(input('Shift Number: '))
    wage = float(input('Hourly Pay: '))

    # Validate shift number as valid #
    while shiftNum < 1 or shiftNum > 3:
        shiftNum = int(input('Please enter a valid shift number (1-3): '))

    # Validate wage input #
    while wage < MINWAGE:
        print('Wage must be at least $' + str(MINWAGE) + ', per Washington State Law.')
        wage = float(input('Enter a legal wage: '))

    # Create object using the input information #
    newEmployee = Employee.ProductionWorker(name, empNum, shiftNum, wage)

    # Print the results #
    print('\nNew employee entry made:\n')
    print('Name:', newEmployee.get_name())
    print('Employee Number:', newEmployee.get_employee_number())
    print('Shift Number:', newEmployee.get_shift_number())
    print('Hourly Pay: $' + format(newEmployee.get_hourly_wage(), '.2f'))


main()
