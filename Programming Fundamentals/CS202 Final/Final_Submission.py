from BookAuthor import BookAuthor

def main():
    # Establish the author object #
    author = BookAuthor('Harris McCall', 'Male', '08/14/2000')

    # Add some books #
    author.add_book('My First book', 'Smart Publishing')
    author.add_book('My Second Book', 'Cool Publishing')

    # Print a list of the books #
    print('Author: ' + author.get_name())
    print('--------------------')
    author.show_books()

    author.remove_book()
    author.show_books()


main()