class Publisher:
    def get_name(self):
        self.__name = input("Enter the publisher name: ")

    def print_name(self):
        print("Publisher's name:", self.__name)


class Book(Publisher):
    def get_book(self):
        self.get_name()
        self.__name = input("Enter the book name: ")
        self.__author = input("Enter author name: ")

    def print_book(self):
        self.print_name()
        print("Book name:", self.__name, "\nAuthor: ", self.__author)


class Python(Book):
    def get_py(self):
        self.get_book()
        self.__pages = input("Enter the number of pages: ")
        self.__price = input("Enter the price of the book: ")

    def print_py(self):
        self.print_book()
        print("Price: ", self.__price, "\nPages: ", self.__pages)


p = Python()
p.get_py()
p.print_py()
