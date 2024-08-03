from Person import Person       # BookAuthor IS A Person
from Book import Book           # BookAuthor HAS Books


class BookAuthor(Person):
    # Construct the instance #
    def __init__(self, name, gender, dateOfBirth):
        super().__init__(name, gender, dateOfBirth)  # Construct Person
        self.__books = []

    # Accessor Methods #
    def show_books(self):
        for i in range(len(self.__books)):
            print('Book #' + str(i+1))
            print(self.__books[i])

    # Mutator Methods #
    def add_book(self, title, publisher):
        # Create a book object to add to the list #
        book = Book(title, publisher)

        # Ask for cover type #
        print('Does', title, 'have a hard cover?')
        cover = input('Y/N: ')

        # Validate entry #
        while cover.upper() != 'Y' and cover.upper() != 'N':
            cover = input('Please enter "Y" or "N": ')

        # Set the book object's cover type using its functions #
        if cover.upper() == 'Y':
            book.is_hard_cover()
        else:
            book.is_soft_cover()

        # Add the book to the list #
        self.__books.append(book)

    def remove_book(self):
        # Print a separating line #
        print('\nRemove tool:')

        # Show books for selection #
        self.show_books()

        # Ask user for selection #
        num = int(input('Enter the number assigned to the book you want to remove: '))

        # Validate user entry #
        while num < 1 or num > len(self.__books) + 1:
            num = int(input('Please enter a valid number: '))

        # Remove the requested entry #
        self.__books.remove(self.__books[num-1])

        # Print a result #
        print('\nBook removed from author!\n')
