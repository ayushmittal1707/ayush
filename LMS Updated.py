def screen_hold():
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


class LibraryInfo:
    def __init__(self, library_id, user_name):
        self.library_id = library_id
        self.name = user_name
        self.library_student_DB = {}
        self.library_staff_DB = {}

    def enrol_student(self, library_id, stu_name):
        self.library_student_DB.update({library_id: stu_name})
        print(f'User {stu_name} is added successfully')

    def enrol_staff(self, library_id, staff_name):
        self.library_staff_DB.update({library_id: staff_name})
        print(f'Staff {staff_name} is added successfully')

    def display_enrol_student(self):
        print('Available students in library are : ', self.library_student_DB)

    def display_enrol_staff(self):
        print('Available staff in library are : ', self.library_staff_DB)


class BookInfo(LibraryInfo):
    """books information"""

    def __init__(self, book_list):
        self.book_list = book_list
        self.bookDB = {}
        LibraryInfo.__init__(self, library_id=1, user_name='awash')

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
            # return False

    def issue_book(self, book_name, library_id):
        self.bookDB.update({library_id: book_name})
        self.book_list.remove(book_name)
        print(f'Book: {book_name} is issued to library id : {library_id}  ')

    def remove_book(self, book_name):
        if book_name in self.book_list:
            self.book_list.remove(book_name)
            print(f'Book : {book_name} is removed successfully')
        else:
            print(f'Book : {book_name} is not available')

    def display_issued_books(self):
        print(self.bookDB)

    def submit_book(self, book_name):
        self.book_list.append(book_name)
        print(f'Book {book_name} is submitted successfully')


boo = BookInfo(['c', 'c++', 'java', 'python', 'database', 'oracle'])
while True:
    print('Welcome to my library. Please Enroll yourself in library')
    print('Press 1 if you are student. Press 2 if you are library staff')
    try:

        choice = int(input())
        if choice == 1:
            print('Hello Student.Press 1 to Signup and Press 2 to Login')

            choice3 = int(input())
            if choice3 == 1:

                lib_id = int(input('Please Enter a Numeric Library Id : '))
                if lib_id in boo.library_student_DB:
                    print('Enter a different Library Id')
                    continue
                else:

                    name = input('Please enter your name : ')
                    boo.enrol_student(lib_id, name)
            elif choice3 == 2:
                lib_id = int(input('Please enter your Library id : '))
                name = input('Enter Your name : ')
                if (lib_id, name) not in boo.library_student_DB.items():
                    print('Enter Right details')
                    continue

            while True:

                print('Please select a choice to go further')
                print('press 1 if you want a new book ')
                print('press 2 to display all available books ')
                print('press 3 if you want to submit previous issued  book ')
                print('Press 4 to go in previous menu ')

                choice1 = int(input())
                if choice1 == 1:
                    Book_name = input('Enter the name of book : ')
                    if boo.book_available(Book_name):
                        lib_id = int(input('Enter your Library Id : '))
                        student_name = input('enter your name : ')
                        if (lib_id, student_name) in boo.library_student_DB.items():
                            boo.issue_book(Book_name, lib_id)
                        else:
                            print('Please Enter Your right details')
                        screen_hold()
                elif choice1 == 2:
                    boo.display_book()
                    screen_hold()
                elif choice1 == 3:
                    Book_name = input('Enter name of the book : ')
                    lib_id = int(input('Enter Library Id : '))
                    if (lib_id, Book_name) in boo.bookDB.items():
                        del boo.bookDB[lib_id]
                        boo.submit_book(Book_name)
                        screen_hold()
                    else:
                        print('Book is not issued to you')
                        screen_hold()
                if choice1 == 4:
                    break
        if choice == 2:
            print('Hello Staff. Press 1 to Signup and Press 2 to Login')
            choice4 = int(input())
            if choice4 == 1:

                lib_id = int(input('Please Enter a Numeric Library Id : '))
                if lib_id in boo.library_staff_DB:
                    print('Enter a different library id')
                    continue
                else:
                    name = input('Please enter your name : ')
                    boo.enrol_staff(lib_id, name)
            elif choice4 == 2:
                lib_id = int(input('Please enter your Library id : '))
                name = input('Enter Your name : ')
                if (lib_id, name) not in boo.library_staff_DB.items():
                    print('Enter Right Details')
                    continue
            while True:

                print('Hello Staff. Please make a choice for further action ')
                print('Press 1 to Add a new book')
                print('press 2 to Remove a book')
                print('press 3 to display All books')
                print('press 4 to display Issued books')
                print('Press 5 to display enrol students in library')
                print('Press 6 to display enrol staff in library')
                print('Press 7 to go in previous menu ')
                choice = int(input())
                if choice == 1:
                    Book_name = input('enter the name of book : ')
                    boo.add_book(Book_name)
                    screen_hold()
                elif choice == 2:
                    Book_name = input('enter the name of book to be removed : ')
                    boo.remove_book(Book_name)
                    screen_hold()
                elif choice == 3:
                    boo.display_book()
                    screen_hold()
                elif choice == 4:
                    boo.display_issued_books()
                    screen_hold()
                elif choice == 5:
                    boo.display_enrol_student()
                    screen_hold()
                elif choice == 6:
                    boo.display_enrol_staff()
                    screen_hold()
                if choice == 7:
                    break

    except ValueError:
        print('Please enter a right Value. Thank You')
    screen_hold()
