import Employee

def main():
    # Collect user input #
    print('Enter an new Shift Supervisor\'s information:')
    name = input('Name: ')
    empNum = int(input('Employee Number: '))
    salary = float(input('Salary: '))
    bonus = float(input('Bonus: '))

    # Create object using the input information #
    newEmployee = Employee.ShiftSupervisor(name, empNum, salary, bonus)

    # Print the results #
    print('\nNew employee entry made:\n')
    print('Name:', newEmployee.get_name())
    print('Employee Number:', newEmployee.get_employee_number())
    print('Salary: $' + format(newEmployee.get_salary(), ',.2f'))
    print('Bonus: $' + format(newEmployee.get_bonus(), ',.2f'))


main()
