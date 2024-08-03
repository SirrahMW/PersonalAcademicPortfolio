class Person:
    def __init__(self, name, gender, dateOfBirth):
        self.__name = name
        self.__gender = gender
        self.__dateOfBirth = dateOfBirth

    # Accessor Methods #
    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_date_of_birth(self):
        return self.__dateOfBirth

    # Mutator Methods #
    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def set_birthday(self, date):
        self.__dateOfBirth = date

    # __str__ #
    def __str__(self):
        return 'Name: ' + self.__name + '\nGender: ' + self.__gender + '\nDate of Birth: ' + self.__dateOfBirth
