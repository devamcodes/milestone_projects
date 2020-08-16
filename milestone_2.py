"""
Project:Book collection.
Author:Devam A

Description:book shop similar to apparel-shop
STATUS:test 1 successful
        test 2 pending
***DONE***1.need help in exiting the program while handling the errors
        2.remove the glitches and TODO's
steps:
1. welcome message
2. main menu
    1.add book
    2.view list
    3.mark as read(make a new list)
    4.remove book
    5.exit program
3. def functions
4. database file import
5.
*Questions:
    1.how to create a temporary database file
"""
MY_BOOKS = []


def add_book():
    user_input_add = input("enter the book name:")
    MY_BOOKS.append(user_input_add)
    print("Book added to MY BOOKS")
    return MY_BOOKS


def view_list(option):
    view_menu = """
     1. list of books
     2. table of list of books
    """
    user_input_view_list = int(input(view_menu))
    # TODO:show the proper list of books with index
    #this feature is not the perfect but it can do the work
    if user_input_view_list == 2:
        for _ in range(len(MY_BOOKS)):
            print(_,MY_BOOKS[_])
    else:
        print(MY_BOOKS)

def mark_as_read():
    user_input_mark_read = input("enter the name of book to mark it as read:")
    #TODO:1. try-except loop is not working properly
    mark_as_read_books = []
    if user_input_mark_read in MY_BOOKS:
        mark_as_read_books.append(user_input_mark_read)
        print(f"{user_input_mark_read} book is added to mark as read.")
    else:
        raise ValueError(f"{user_input_mark_read} book is not in your book list")

def remove_book():
#TODO:show the list of books in columns and rows
    print(MY_BOOKS)
    user_input_remove_book = int(input("enter the book index to remove the book:"))
    MY_BOOKS.pop(user_input_remove_book)
    print(f"{user_input_remove_book} is removed from the list.")



main_menu = """
1. Add book to MY BOOKS
2. View My BOOKS
3. Mark the book as read
4. Remove the book
5. Exit the program
enter the index number 
-->"""
user_name = input("enter your name:")
user_name_boolean = bool(user_name)

if user_name_boolean == True:
    print(f"Hello,{user_name}")
else:
    raise ValueError("Invalid User Name!! Please Enter A Valid Name:")
user_input_menu = int(input(main_menu))
try:
    while user_input_menu != 0:

#TODO:program should complete at 5 and error should be also handled if pressed any thingelse
        if user_input_menu == 1:
            add_book()
        elif user_input_menu == 2:
            view_list(option = 0)
        elif user_input_menu == 3:
            mark_as_read()
        elif user_input_menu == 4:
            remove_book()
        elif user_input_menu == 5:
            print("exiting the program!! ")
            break
        user_input_menu = int(input(main_menu))
    else :
        print("Exiting the program")
except:
    raise ValueError("Invalid Input!! Try again.")
