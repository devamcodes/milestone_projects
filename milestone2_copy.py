"""
Project: learn database from the course
Author: This is the copied code

Description:This project is better than milestone2
status:
1. one error occurred in viewing the list(option 2)
2. one todo added.
test 1 --> successful with exception
test 2-->
"""
from utils import database
from utils.database import My_Books

main_menu = """
MAIN MENU:
1. Add book to MY BOOKS
2. View My BOOKS
3. Mark the book as read
4. Remove the book
5. Exit the program
enter the index number 
-->"""



def add_the_book():
    name = input("enter the book name:")
    author = input("enter the author name:")
    database.add_book(name, author)
    print(f"The {name} book is added to MY BOOKS.")


def view_book_list():
    database.My_Books()
    for books in My_Books:
        read ='YES' if books['read'] else 'NO'
        print(f"{books['name']} by author{books['author']}, read{books['read']}.")


def mark_book_as_read():
    name = input("enter the name of the book:")
    database.mark_as_read(name)
    print(f"The {name} book is marked as read. ")


def remove_the_book():
    book_name = input("enter the book name you want to remove:")
    database.remove_book(book_name)
    print(f"The {book_name} book is removed from MY BOOKS.")


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
        view_book_list()#error occured: list is not callable.
    elif user_input == 3:
        mark_book_as_read()
    elif user_input == 4:
        remove_the_book()
    else:
        raise ValueError("Invalid Input!! Please enter the valid value...")
    user_input = int(input(main_menu))
else:
    print("The program terminated...")
    print("Exiting the program...........")
