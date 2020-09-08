"""
Project: learn database from the course
Author: Devam A

Description:This project is better than milestone2
status:
1. try to add history function.a function which takes input from My_books but dont get affected from any function of the code it tracks all adds, markasreads, removes.
2. one "todo". remaining
3. error occurred :- if you run the program for the first time and you don't add a book but you try to mark a book as read which is already added.
4. if i add some data outside the pycharm directly in the file then it raise index error list index out of range.
5. if a book is not present or maybe present in the list and if you call for mark as read function it remove all the data from the database file.
test 1 --> successful with exception
test 2--> partially successful.
test 3--> partly successful
"""
from utils import database


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
    database.add_book(name, author)
    print(f"The {name} book written by is added to MY BOOKS.")


def view_book_list():
    method = """
    1. view books as statement form
    2. view books as tabular form
    """
    user_input_for_view_books = int(input(method))
    if user_input_for_view_books == 1:
        for books in database.view_books():
            read = 'Yes' if books['read'] == '1' else 'No'
            print(f"The {books['name']} book is written by author {books['author']},you have {read} this book.")
    elif user_input_for_view_books == 2:
        for books in database.view_books():
            read = 'No' if books['read'] == '0' else 'Yes'
            print(f"{books['name']} || {books['author']}  || {read}")

    else:
        raise ValueError("Invalid input!!! Please try again....")

def mark_book_as_read_or_unread():
    method ="""
    1. Mark the book as read.
    2. Mark the book as unread.
    -->"""
    database.create_books_table()
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
    elif user_input == 4:
        remove_the_book()
    else:
        raise ValueError("Invalid Input!! Please enter the valid value...")
    user_input = int(input(main_menu))
else:
    print("The program terminated...")
    print("Exiting the program...........")
