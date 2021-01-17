class LibraryInfo:
    def __init__(self, book_list, name):
        self.book_list = book_list
        self.book = name
        self.booksDB = {}

    def display_book(self):
        print('Available Books in Library Are : ')
        for book in self.book_list:
            print(book)

    def add_book(self, book):
        self.book_list.append(book)
        print('book is added ')

    def book_available(self, book):
        if book in self.book_list:
            return True
        else:
            print('Book is not available')

    def issue_book(self, user, book):
        self.booksDB.update({book: user})
        self.book_list.remove(book)
        print(f'Book is issued to {self.booksDB[book]}')

    def remove_book(self, book):
        if book in self.book_list:
            self.book_list.remove(book)
            print(f'{book} has removed successfully ')

    def display_issued_books(self):
        print(self.booksDB)


lib = LibraryInfo(['c', 'c++', 'java', 'python', 'database', 'oracle'], 'manoj')

while True:
    print('welcome to my library. please Enter a choice :')
    print("""Press 1 for User 2 for Staff""")
    try:
        choice1 = int(input())
        if choice1 == 1:
            print('Hello user. Select a choice to go further :')
            print('press 1 if you want a new book ')
            print('press 2 to display all available books ')
            print('press 3 if you want to submit previous issued  book ')
            choice = int(input())
            if choice == 1:
                book_name = input('enter the name of the book : ')
                if lib.book_available(book_name):
                    user_name = input('enter your name : ')
                    lib.issue_book(user_name, book_name)
                    lib.remove_book(book_name)
            elif choice == 2:
                # print('Available books in library are : ')
                lib.display_book()
            if choice == 3:
                book_name = input('enter the name of book : ')
                user_name = input('enter your name ')
                if book_name in lib.booksDB:

                    del lib.booksDB['user_name']
                    lib.add_book(book_name)
                    print('book has been submitted successfully ')
                else:
                    print('Book is not issued to you ')
        if choice1 == 2:
            print('Hello Staff. Please make a choice for further action ')
            print('Press 1 to Add a new book')
            print('press 2 to Remove a book')
            print('press 3 to display All books')
            print('press 4 to display Issued books')
            choice = int(input())
            if choice == 1:
                book_name = input('enter the name of book : ')
                lib.add_book(book_name)
            elif choice == 2:
                book_name = input('enter the name of book to be removed : ')
                lib.remove_book(book_name)
            elif choice == 3:
                lib.display_book()
            if choice == 4:
                lib.display_issued_books()
    except ValueError:
        print('enter a right choice : ')
    print('Enter q to exit and c to continue.')
    choice2 = ''
    while choice2 != 'c' and choice2 != 'q':

        choice2 = input()
        if choice2 == 'q':
            exit()
        elif choice2 == 'c':
            continue
        else:
            print('enter a right choice')
