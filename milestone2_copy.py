"""
Project: learn database from the course
Author: This is the copied code

Description:This project is better than milestone2
status:
1. one error occurred in viewing the list(option 2)***REMOVED***
2. two todo added.
test 1 --> successful with exception
test 2--> partially successful.
test 3-->
"""
from utils import database
from utils.database import My_Books

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
    database.add_book(name, author)#TODO: error occurred "list.remove():x not in list" even book was shown in view books option.
    print(f"The {name} book is added to MY BOOKS.")


def view_book_list():
    database.view_books()
    for books in My_Books:
        read = 'YES' if books['read'] else 'NO'
        print(f"The {books['name']} book is written by author {books['author']},you have read this book -->{read}.")


def mark_book_as_read_or_unread():
    method ="""
    1. Mark the book as read.
    2. Mark the book as unread.
    """
    user_chioce = int(input(method))
    if user_chioce == 1:
        name = input("enter the name of the book:")
        database.mark_as_read(name)
        print(f"The {name} book is marked as read. ")
    elif user_chioce == 2:
        name = input("enter the author name:")
        database.mark_as_unread(name)
        print(f"The book {name} is marked as unread.")
    else:
        raise ValueError("Please enter the valid input.")

def remove_the_book():
    name = input("enter the book name you want to remove:")
    database.remove_book(name)
    print(f"The {name} book is removed from MY BOOKS.")


#todo:learn how to import this user_name function from user_name.py.
user_name = input("Enter your name:")
user_name_boolean = bool(user_name)
if user_name_boolean == True:
    print(f"Hello,{user_name.title()}")
else:
    raise ValueError("Invalid User Name!! Please Enter A Valid Name:")

user_input = int(input(main_menu))
while user_input != 5:
    if user_input == 1:
        add_the_book()
    elif user_input == 2:
        view_book_list()
    elif user_input == 3:
        mark_book_as_read_or_unread()
    elif user_input == 4:#Todo:once this function was called and again used option one but still book didnt get added to the list and then code malfunctions
        remove_the_book()
    else:
        raise ValueError("Invalid Input!! Please enter the valid value...")
    user_input = int(input(main_menu))
else:
    print("The program terminated...")
    print("Exiting the program...........")
