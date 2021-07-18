"""
Project: learn database from the course
Author: Devam A

Description:This project is better than milestone2
status:
1. try to add history function.a function which takes input from My_books but dont get affected from any function of the code it tracks all adds, markasreads, removes.
3. error occurred :- if you run the program for the first time and you don't add a book but you try to mark a book as read which is already added.
4. if i add some data outside the pycharm directly in the file then it raise index error list index out of range.
5. if a book is not present or maybe present in the list and if you call for mark as read function it remove all the data from the database file.
test 1 --> successful with exception
test 2--> partially successful.
test 3--> partly successful
ERROR FOUND: In the while loop error handling is not employed, the program crashes there.
"""
from utils import Database_Library


main_menu = """
MAIN MENU:
1. Add book to MY BOOKS
2. View My BOOKS
3. Mark the book as read or unread
4. Remove the book
5. Exit the program
enter the index number 
-->"""


def add_the_book():
    name = input("enter the book name:")
    author = input("enter the author name:")
    Database_Library.add_book(name, author)
    print(f"The {name} book written by {author} is added to MY BOOKS.")


def view_book_list():
    method = """
    1. view books as statement form
    2. view books as tabular form
    """
    user_input_for_view_books = int(input(method))
    if user_input_for_view_books == 1:
        for books in Database_Library.view_books():
            read = 'Read' if books['read'] else 'Not read'
            print(f"The {books['name']} book is written by author {books['author']},you have {read} this book.")
    elif user_input_for_view_books == 2:
        for books in Database_Library.view_books():
            read = 'Read' if books['read'] else 'Not read'
            print(f"{books['name']} || {books['author']}  || {read}")

    else:
        raise ValueError("Invalid input!!! Please try again....")

def mark_book_as_read_or_unread():
    method ="""
    1. Mark the book as read.
    2. Mark the book as unread.
    -->"""

    user_choice = int(input(method))
    if user_choice == 1:
        try:
            name = input("enter the name of the book:")
            Database_Library.mark_as_read(name)
            print(f"The {name} book is marked as read. ")
        except:
            raise ValueError("Book not found in My Books!!!Try again..")
    elif user_choice == 2:
        try:
            name = input("enter the book name:")
            author = input("enter the author name:")
            Database_Library.mark_as_unread(name, author)
            print(f"The book {name} is marked as unread.")
        except:
            raise ValueError("Book not found!!Please try again..")
    else:
        raise ValueError("Please enter the valid input.")
#if i remove any book outside of my books then it should raise the error.
def remove_the_book():
    name = input("enter the book name you want to remove:")

    Database_Library.remove_book(name)
    print(f"The {name} book is removed from MY BOOKS.")


def user_name():
    user_name_input = input("Enter your name:")
    user_name_boolean = bool(user_name_input)
    while user_name_boolean != True:
        print("Incorrect UserName: Please enter the correct user name")
        user_name_boolean = bool(input("Enter your name:"))
    print(f"Hello,{user_name_input.title()}")

# user_input = int(input(main_menu))
Database_Library.create_books_tables()
#if i directly enter the book name in th main menu then the program crashes so need to handle the error

# user_name()
# while user_input != 5:
#     if user_input == 1:
#         add_the_book()
#     elif user_input == 2:
#         view_book_list()
#     elif user_input == 3:
#         mark_book_as_read_or_unread()
#     elif user_input == 4:
#         remove_the_book()
#     else:
#         raise ValueError("Invalid Input!! Please enter the valid value...")
#     user_input = int(input(main_menu))
# else:
#     print("The program terminated...")
#     print("Exiting the program...........")


#####
user_name()
try:
    user_input = int(input(main_menu))
    while user_input != 5:
        try:
            if user_input == 1:
                add_the_book()
            elif user_input == 2:
                view_book_list()
            elif user_input == 3:
                mark_book_as_read_or_unread()
            elif user_input == 4:
                remove_the_book()
            else:
                print("Error occurred...")
                input("Press any to run the program again.")
            user_input = int(input(main_menu))

        except:
            input("Invalid Input!! try again...")
            user_input = int(input(main_menu))

except:
    input("Error occurred while getting the input pls try with the valid input. press any key to continue.")
    try:
        user_input = int(input(main_menu))
        while user_input != 5:
            # TODO:if enter is pressed instead of any number then raise an error.

            # TODO:if enter is pressed without any value then error should raise and loop should continue.
            try:
                if user_input == 1:
                    add_the_book()
                elif user_input == 2:
                    view_book_list()
                elif user_input == 3:
                    mark_book_as_read_or_unread()
                elif user_input == 4:
                    remove_the_book()
                else:
                    print("Error occurred...")
                    input("Press any to run the program again.")
                user_input = int(input(main_menu))

            except:
                print("Invalid Input!! try again...")
                user_input = int(input(main_menu))


    except:
        raise ValueError("Multiple Invalid inputs!!! Please try again by run the program from the start...")

