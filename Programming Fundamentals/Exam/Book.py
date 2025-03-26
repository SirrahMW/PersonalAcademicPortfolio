class Book:
    # Construct the instance #
    def __init__(self, title, publisher, hardCover=False):
        self.__title = title
        self.__publisher = publisher
        self.__hardCover = hardCover
        
    # Accessor Methods #
    def get_title(self):
        return self.__title
    
    def get_publisher(self):
        return self.__publisher

    # Return a string based on hardCover bool #
    def cover_type(self):
        if not self.__hardCover:
            return 'Soft Cover'

        elif self.__hardCover:
            return 'Hard Cover'

    # Mutator Methods #
    def set_title(self, title):
        self.__title = title
        
    def set_publisher(self, publisher):
        self.__publisher = publisher
        
    def is_hard_cover(self):
        self.__hardCover = True

    def is_soft_cover(self):
        self.__hardCover = False

    # __str__  to check the state of the oject #
    def __str__(self):
        return 'Title: ' + self.__title +'\nPublisher: ' + self.__publisher + '\nCover type: ' + self.cover_type() + '\n'
