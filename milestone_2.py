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

"""
1. create a database file  and add all the functions in the file except the main menu function
2. mark as read function can be improvised a different list should be created. 
3. 
"""


def add_book():
    user_input_add = input("enter the book name:")
    MY_BOOKS.append(user_input_add)
    print("Book added to MY BOOKS")
    user_input_menu = 0
    return MY_BOOKS


def view_list():
    # A simple list would be enough to view a book collection instead in removebook books with index numbers is good.
    print(MY_BOOKS)
    user_input_menu = 0


def mark_as_read():
    user_input_mark_read = input("enter the name of book to mark it as read:")
    mark_as_read_books = []
    if user_input_mark_read in MY_BOOKS:
        mark_as_read_books.append(user_input_mark_read)
        print(f"{user_input_mark_read} book is added to mark as read.")
        user_input_menu = 0
    else:
        raise ValueError(f"{user_input_mark_read} book is not in your book list")


def remove_book():
        for count, books in enumerate(MY_BOOKS,1):
            print(count, books)
        user_input_remove_book = input("enter the book name to remove the book:")
        if user_input_remove_book in MY_BOOKS:
            MY_BOOKS.remove(user_input_remove_book)
            print(f"{user_input_remove_book} is removed from the list.")
            user_input_menu = 0
        else:
            raise ValueError("Book not found!! Enter correct book name to remove from your list. Try again...")


main_menu = """
MAIN MENU:
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
user_input_menu_bool = bool(user_input_menu)
if user_input_menu_bool == True:
    #error is not working properly.
    try:
        while user_input_menu == 0:
            """Idea--> cereate a function that exits the program which gives the value to while loop to end 
            and at the end of other functions give the value 0 to while loop to resolve the error."""

    #TODO:program should complete at 5 and error should be also handled if pressed any thing else.
            if user_input_menu == 1:
                add_book()
            elif user_input_menu == 2:
                view_list()
            elif user_input_menu == 3:
                mark_as_read()
                #todo:if book is not found the error is raised but along with that another error at line 104 raises which should be resolved
            elif user_input_menu == 4:
                remove_book()
            elif user_input_menu == 5:
                print("exiting the program!! ")
                break
            user_input_menu = int(input(main_menu))
        else :
            print("Exiting the program")
            raise ValueError("Incorrect Input!!!")
    except:
        raise ValueError("Invalid Input!! Try again...")
    else:
        print("exiting the program")
else:
    raise ValueError("Invalid Input!! please enter a valid input.")