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


main_menu = """
MAIN MENU:
1. Add book to MY BOOKS
2. View My BOOKS
3. Mark the book as read
4. Remove the book
5. Exit the program
enter the index number 
-->"""
def user_name():
    user_name_input = input("Enter your name:")
    user_name_boolean = bool(user_name_input)
    while user_name_boolean != True:
        print("Incorrect UserName: Please enter the correct user name")
        user_name_boolean = bool(input("Enter your name:"))
    print(f"Hello,{user_name_input.title()}")

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


user_name()

try:
    user_input = int(input(main_menu))
    while user_input != 5:
        try:
            if user_input == 1:
                add_book()
            elif user_input == 2:#todo:try to use split method to remove the book from the list, you can display the book without any qoutes or brackets
                view_list()
            elif user_input == 3:#todo: The book is marked as read this should be show in the console to the user.
                mark_as_read()
            elif user_input == 4:
                remove_book()
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
                    add_book()
                elif user_input == 2:
                    print()
                elif user_input == 3:
                    mark_as_read()
                elif user_input == 4:
                    remove_book()
                else:
                    print("Error occurred...")
                    input("Press any to run the program again.")
                    user_input = int(input(main_menu))

            except:
                print("Invalid Input!! try again...")
                user_input = int(input(main_menu))


    except:
        raise ValueError("Multiple Invalid inputs!!! Please try again by run the program from the start...")

