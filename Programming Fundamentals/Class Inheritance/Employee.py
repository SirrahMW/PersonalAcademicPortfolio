class Employee:
    def __init__(self, name, empNumber):
        self.__name = name
        self.__num = empNumber

    def get_name(self):
        return self.__name

    def get_employee_number(self):
        return self.__num

    def set_name(self, name):
        self.__name = name

    def set_employee_number(self, num):
        self.__num = num


class ProductionWorker(Employee):
    def __init__(self, name, empNumber, shiftNumber, hourlyWage):
        Employee.__init__(self, name, empNumber)
        self.__shiftNumber = shiftNumber
        self.__hourlyWage = hourlyWage

    def get_shift_number(self):
        return self.__shiftNumber

    def get_hourly_wage(self):
        return self.__hourlyWage

    def set_shift_number(self, num):
        self.__shiftNumber = num

    def set_hourly_wage(self, wage):
        self.__hourlyWage = wage


class ShiftSupervisor(Employee):
    def __init__(self, name, empNumber, salary, bonus):
        Employee.__init__(self, name, empNumber)
        self.__salary = salary
        self.__bonus = bonus

    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus

    def set_salary(self, salary):
        self.__salary = salary

    def set_bonus(self, bonus):
        self.__bonus = bonus
