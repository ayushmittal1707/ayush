class LibraryInfo:
    """validate user and staff"""

    def __init__(self, library_id, password):
        self.library_id = library_id
        self.password = password
        self.libraryDB = {}

    def user_register(self, library_id, password):
        self.libraryDB.update({library_id: password})
        print('you are successfully registered in library')



    def staff_register(self, ):
        pass


class StaffInfo(LibraryInfo):
    def __init__(self):
        LibraryInfo.__init__(self, 2, 123)


class BookInfo(LibraryInfo):
    """books information"""

    def __init__(self, book_list, library_id, password):
        self.book_list = book_list
        self.bookDB = {}
        LibraryInfo.__init__(self, library_id, password)

        # super().__init__(library_id  )

    def add_book(self, book_name):
        self.book_list.append(book_name)
        print('Book is added successfully')

    def display_book(self):
        print('Available Books in library are : ')
        for book in self.book_list:
            print(book)

    def book_available(self, book_name):
        if book_name in self.book_list:
            return True
        else:
            print(f'Book: {book_name} is Not available in Library')

    def issue_book(self, book_name, user_id):
        self.bookDB.update({user_id: book_name})
        self.book_list.remove(book_name)
        print(f'Book: {book_name} is issued to user_id: {user_id}  ')

    def remove_book(self, book_name):
        if book_name in self.bookDB:
            self.book_list.remove(book_name)
            print(f'Book : {book_name} is removed successfully')
        else:
            print(f'Book : {book_name} is not available')

    def display_issued_books(self):
        print(self.bookDB)


# lib = LibraryInfo(1, 1234)

boo = BookInfo(['c', 'c++', 'java', 'dbms', 'asp', 'dsa', 'python'], 1, 1234)

while True:
    print('Welcome to My Library. Please select a choice')
    print('Press 1 for Log in. Press 2 for signup. press 3 for staff ')
    try:
        choice = int(input('Enter Your Choice : '))
        if choice == 1:
            try:

                login_id = int(input('Enter Your login Id : '))

                if login_id in boo.libraryDB:

                    login_password = input('Enter your Login Password: ')

                    print('Hello user. Select a choice to go further :')
                    print('press 1 Requesting a new book ')
                    print('press 2 to display all available books ')
                    print('press 3 if you want to submit previous issued  book ')
                    try:
                        choice1 = int(input())
                        if choice1 == 1:
                            bookName = input('Enter name of book')
                            if bookName in boo.book_list:
                                user_Id = input('Enter Your Id : ')
                                boo.issue_book(bookName, user_Id)
                                boo.remove_book(bookName)
                            else:
                                print('Book is Not available')
                        elif choice1 == 2:
                            boo.display_book()
                        if choice1 == 3:
                            bookName = input('Enter name of book : ')
                            user_Id = input('Enter Your Id : ')
                            if bookName in boo.bookDB:
                                del boo.bookDB['user_id']
                                boo.add_book(bookName)
                                print(f'Book: {bookName}  issued to Id: {user_Id} is submitted successfully.')
                            else:
                                print('Book is not issued to you')

                    except ValueError:
                        print('Enter a right choice')
                else:
                    print('enter right log in Id and Password')
            except ValueError:
                print('Enter right value for id')
        if choice == 2:
            print('Enter below details : ')
            try:
                login_id = int(input('Enter Your log in Id : '))
                if login_id not in boo.libraryDB:
                    login_password = input('Enter your password : ')
                    boo.user_register(login_id, login_password)
                    print('Thank you for sign up. Please make a choice for go further')
                    print('Hello user. Select a choice to go further :')
                    print('press 1 Requesting a new book ')
                    print('press 2 to display all available books ')
                    print('press 3 if you want to submit previous issued  book ')
                    try:
                        choice1 = int(input())
                        if choice1 == 1:
                            bookName = input('Enter name of book')
                            if bookName in boo.book_list:
                                user_Id = input('Enter Your Id : ')
                                boo.issue_book(bookName, user_Id)
                                boo.remove_book(bookName)
                            else:
                                print('Book is Not available')
                        elif choice1 == 2:
                            boo.display_book()
                        if choice1 == 3:
                            bookName = input('Enter name of book : ')
                            user_Id = input('Enter Your Id : ')
                            if bookName in boo.bookDB:
                                del boo.bookDB['user_id']
                                boo.add_book(bookName)
                                print(f'Book: {bookName}  issued to Id: {user_Id} is submitted successfully.')
                            else:
                                print('Book is not issued to you')

                    except ValueError:
                        print('Enter a right choice')
                else:
                    print('Log id is using by Other user. Try a different')

            except ValueError:
                print('Login Id Should be integer')
        if choice == 3:
            pass

    except ValueError:
        pass
